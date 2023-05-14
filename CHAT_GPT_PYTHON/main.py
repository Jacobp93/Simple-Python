import openai
import click
import os

openai.api_key = "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"  # Replace with your actual OpenAI API key

def get_gpt3_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3000,
        temperature=1.5,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def print_banner():
    banner = """

    """
    print(banner)
    print("Welcome to Chat GPT!\n")

@click.command()
def main():
    clear_terminal()
    print_banner()

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            break

        prompt = f"You: {user_input}\nAI: "
        response = get_gpt3_response(prompt)
        print("AI:", response)

if __name__ == "__main__":
    main()
