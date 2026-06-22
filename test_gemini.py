import os
from google import genai

# Create a Gemini client using your API key from environment variables
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Send a simple text prompt to confirm the connection works
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello and confirm you are Gemini 2.5 Flash.",
)

# Print the model's response
print(response.text)
