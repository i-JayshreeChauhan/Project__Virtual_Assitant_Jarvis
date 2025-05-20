from google import genai

client = genai.Client(api_key="AIzaSyBLWPvsytYZO2SM4S4Nle9OZ6rilaK1jY4")
chat = client.chats.create(model="gemini-2.0-flash")

response = chat.send_message("My name is jayshree")
#print(response.text)

response = chat.send_message("i live in surat")
#print(response.text)

for message in chat.get_history():
    print(f'role - {message.role}',end=": ")
    print(message.parts[0].text)