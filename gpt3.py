import openai

openai.api_key = "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"

while True:
    prompt = input("Prompt")
    if 'exit' in prompt or 'quit' in prompt :
        break

    completion = openai.Completion.create(
        model = "text-davinci-003",
        prompt = prompt,
        max_tokens= 4000,
        n = 1,

    )

    response = completion.choices[0].text

    print(response)
