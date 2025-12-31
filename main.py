
import google.generativeai as genai

genai.configure(api_key="AIzaSyBzWE-K8k5wyGgvELcdDp5pQEInUYa30fE")

apple=genai.GenerativeModel("gemini-2.5-flash")
chat=apple.start_chat(history=[])
print("hi! i am apple the chatbot")
while True:

    user_input = input("user :")
    if user_input.lower()=="bye":
       break
 
    response=chat.send_message(user_input)
    print("apple :",response.text)
