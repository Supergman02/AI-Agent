import os
from dotenv import load_dotenv
from google import genai
import sys

def main():
    print("Hello from ai-agent!")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    print(f"sys.argv: {sys.argv}")
    if len(sys.argv) == 1:
        print("Please give a prompt")
        sys.exit(1)
    response = client.models.generate_content(
        model ='gemini-2.0-flash-001', contents = sys.argv
)
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
