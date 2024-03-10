import openai


openai.api_key = "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"

def chat_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content'].strip()



if __name__ == "__main__":
    user_name = input("what's your name ? : ")
    while True:
        user_input = input( user_name + ": ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_gpt(user_input)
        print("Chat_cat:", response)



#base on chatgpt library 