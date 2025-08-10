# simple chat with chatgpt

from openai import OpenAI

client = OpenAI(
    api_key="<METIS-API-KEY>",
    base_url="https://api.tapsage.com/openai/v1"
)


def ask_ai(input):
    messages = [
        {"role": "system", "content": "you are ai assistant; explain"},
        {"role": "user", "content": input},
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.1,
        messages=messages
    )

    result = response.choices[0].message.content
    return result


def ai_cli():
    while 1:
        user_input = input(">")
        output = ask_ai(user_input)
        print(output)
        print()


ai_cli()
