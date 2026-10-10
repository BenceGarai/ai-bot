import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

def generate_content(client, messages):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages
    )
    # Token use
    if response.usage == None:
        raise RuntimeError("Failed to reach OpenAI")
    
    return response
    
def verbose_output(user_prompt, response):
    print("User prompt: ", user_prompt)
    print("Prompt tokens: ", response.usage.prompt_tokens)
    print("Response tokens: ", response.usage.completion_tokens)
    
def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)
    
    messages = [
        {"role": "user", "content": args.user_prompt},
    ]
    response = generate_content(client, messages)
    
    if args.verbose:
        verbose_output(args.user_prompt, response)
        
    print(response.choices[0].message.content)
        
if __name__ == "__main__":
    main()
