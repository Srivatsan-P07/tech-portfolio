import google.generativeai as genai
import os
from dotenv import load_dotenv

# WARNING: Do not do this in production code.
# This is for quick testing only.

load_dotenv() # Load environment variables from .env file

API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables. Please set it in a .env file or directly.")

print("Supported models for 'generateContent':")
for m in genai.list_models():
  # The 'generateContent' method is the one used for chat and text generation
  if 'generateContent' in m.supported_generation_methods:
    print(f"- {m.name}")


# Now you can use the model
model = genai.GenerativeModel('gemini-1.5-flash-latest')
response = model.generate_content("Give me the plot of the movie interstellar within 10 sentence")

print(response.text)