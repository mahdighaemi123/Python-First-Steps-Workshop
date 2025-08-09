# simple chat with chatgpt + simple memmory

from openai import OpenAI

client = OpenAI(
    api_key="<METIS-API-KEY>",
    base_url="https://api.tapsage.com/openai/v1"
)

messages = [
    {"role": "system", "content": "you are ai assistant"},
]


def ask_ai(input):
    messages.append({"role": "user", "content": input})

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    result = response.choices[0].message.content

    messages.append({"role": "assistant", "content": result})
    return result


def ai_cli():
    while 1:
        user_input = input(">")
        output = ask_ai(user_input)
        print(output)
        print()


ai_cli()
