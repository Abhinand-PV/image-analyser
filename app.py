import streamlit as st
from google import genai
from google.genai import types

# Initialize the Gemini client using Streamlit's secrets
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# Set which Gemini model to use
MODEL_ID = "gemini-2.5-flash"

# Configure the page layout and title
st.set_page_config(
    page_title="Image Intelligence",
    page_icon="🔍",
    layout="wide"
)
st.title("Image Intelligence")
st.caption("Powered by Google Gemini 2.5 Flash")

# Sidebar lets users pick an analysis mode
mode = st.sidebar.radio(
    "Analysis Mode",
    ["Image Description"]
)
# Store prompts in a dictionary keyed by mode name
PROMPTS = {
    "Image Description": (
        "Analyze this image in detail. Describe what you see including objects, "
        "people, colors, setting, mood, any text visible, and notable details. "
        "Provide a comprehensive, well-organized description."
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

            # Send the image and prompt to Gemini
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=[
                    types.Part.from_bytes(data=image_bytes, mime_type=uploaded_file.type),
                    prompt,
                ],
            )

            # Display the AI's description as formatted markdown
            st.markdown(response.text)
else:
    st.info("Upload an image to get started. Select an analysis mode from the sidebar.")
