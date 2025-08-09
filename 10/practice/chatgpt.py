# simple chat with chatgpt + simple memmory
from openai import OpenAI


client = OpenAI(
    api_key="tpsg-xerSz76No7k9cSJJvNnvXh6jRsFYXyw",
    base_url="https://api.tapsage.com/openai/v1"
)

messages = [
    {"role": "system", "content": "you are ai assistant - همه چی رو کامل و مرحله به مرحله توضیح بده"},
]


def ask_ai(input):
    messages.append({"role": "user", "content": input})

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=messages
    )

    result = response.choices[0].message.content

    messages.append({"role": "assistant", "content": result})
    return result