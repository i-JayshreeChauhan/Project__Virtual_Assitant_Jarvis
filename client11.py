from google import genai

client = genai.Client(api_key="<api-key>")
chat = client.chats.create(model="gemini-2.0-flash")

response = chat.send_message("My name is jayshree")
#print(response.text)

response = chat.send_message("i live in surat")
#print(response.text)

for message in chat.get_history():
    print(f'role - {message.role}',end=": ")
    print(message.parts[0].text)