import streamlit as st
from google import genai
from google.genai import types

# Initialize the Gemini client using Streamlit's secrets
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# Set which Gemini model to use
MODEL_ID = "gemini-2.5-flash"

# Configure the page layout and title
st.set_page_config(
    page_title="Intelligent image classification and analysis",
    page_icon="🔍",
    layout="wide"
)
st.title("Intelligent image classification and analysis")
st.caption("Powered using Gemini 2.5 Flash")

# Sidebar lets users pick an analysis mode
mode = st.sidebar.radio(
    "Analysis Mode",
    ["Image Description","Structured Data Extraction","Stock Chart Analysis"]
)
# Store prompts in a dictionary keyed by mode name
PROMPTS = {
    "Image Description": (
        "Analyze this image in detail. Describe what you see including objects, "
        "people, colors, setting, mood, any text visible, and notable details. "
        "Provide a comprehensive, well-organized description."
    ),
    "Structured Data Extraction": (
        "Extract all structured data from this image and return it as JSON. "
        "If it is a receipt, extract: store_name, date, items (each with name, "
        "quantity, price), subtotal, tax, total. "
        "If it is a business card, extract: name, title, company, email, phone, "
        "address, website. "
        "If it is another document type, extract all relevant fields. "
        "Return only valid JSON with no additional text."
    ),
    "Stock Chart Analysis": (
        "You are a technical analyst. Analyze this stock chart image and provide:\n"
        "1. **Trend**: Overall trend direction (bullish, bearish, or sideways) and reasoning\n"
        "2. **Patterns**: Any chart patterns visible (e.g., head and shoulders, double top/bottom, triangles, flags)\n"
        "3. **Key Levels**: Support and resistance levels you can identify\n"
        "4. **Indicators**: Any visible technical indicators and what they suggest (moving averages, RSI, MACD, volume)\n"
        "5. **Summary**: A brief overall assessment and potential outlook\n\n"
        "Base your analysis only on what is visible in the chart image."
    ),
}

# File uploader accepts common image formats
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png", "webp"],
    help="Supported formats: JPEG, PNG, WEBP"
)
if uploaded_file is not None:
    # Read the raw bytes from the uploaded image
    image_bytes = uploaded_file.read()

    # Create a two-column layout
    col1, col2 = st.columns(2)

    with col1:
        # Display the uploaded image on the left
        st.image(image_bytes, caption="Uploaded Image", use_container_width=True)

    with col2:
        # Show a spinner while Gemini processes the image
        with st.spinner("Analyzing image..."):
            prompt = PROMPTS[mode]

            if mode == "Structured Data Extraction":
                response = client.models.generate_content(
                    model=MODEL_ID,
                    contents=[
                        types.Part.from_bytes(data=image_bytes, mime_type=uploaded_file.type),
                        prompt,
                    ],
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json"
                    ),
                )
            else:
                response = client.models.generate_content(
                    model=MODEL_ID,
                    contents=[
                        types.Part.from_bytes(data=image_bytes, mime_type=uploaded_file.type),
                        prompt,
                    ],
                )


            # Display the AI's description as formatted markdown
            if mode == "Structured Data Extraction":
                import json
                try:
                    data = json.loads(response.text)
                    st.json(data)
                except json.JSONDecodeError:
                    st.code(response.text, language="json")
            else:
                st.markdown(response.text)
else:
    st.info("Upload an image to get started. Select an analysis mode from the sidebar.")
