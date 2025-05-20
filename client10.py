from google import genai

client = genai.Client(api_key="AIzaSyBLWPvsytYZO2SM4S4Nle9OZ6rilaK1jY4")


response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="what is today's date and current time in epoch format",
)

print(response.text)