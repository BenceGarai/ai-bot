import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
import json
from prompts import system_prompt
from call_function import available_functions, call_function


def generate_content(client, messages):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
        temperature=0,
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
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]
    response = generate_content(client, messages)

    is_verbose = args.verbose
    if is_verbose:
        verbose_output(args.user_prompt, response)

    message = response.choices[0].message
    # Tool calls
    if not message.tool_calls:
        print(message.content)
    else:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, is_verbose)
            if result_message["content"] and is_verbose:
                print(f"-> {result_message['content']}")


if __name__ == "__main__":
    main()
