import openai


openai.api_key = "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"

while True:
    prompt = input("Prompt")
    if 'exit' in prompt or 'quit' in prompt :
        break
    MODEL = "gpt-3.5-turbo-0301"
    completion = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "user", "content":prompt}],
        max_tokens= 4000,
        n = 1,

    )

    print(completion.choices[0].message)
    print(completion.choices[0].message.content)
