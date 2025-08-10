# simple chat with chatgpt + read input and write output in file 

from openai import OpenAI

client = OpenAI(
    api_key="<METIS-API-KEY>",
    base_url="https://api.tapsage.com/openai/v1"
)


def ask_ai():

    with open("input.txt", encoding="utf8") as file:
        input = file.read()

    messages = [
        {"role": "system", "content": "you are ai assistant - ریاضیات کاربر رو واسش انجام نده بهش بگو خودش تمرین کنه"},
        {"role": "user", "content": input},
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    result = response.choices[0].message.content

    with open("output.txt", "w", encoding="utf8") as file:
        file.write(result)

    return result


def ai_cli():
    output = ask_ai()
    print(output)
    print()


ai_cli()