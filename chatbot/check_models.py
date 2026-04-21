from google import genai

client = genai.Client(api_key="AIzaSyDczgFPKkeYQSspz7mdDnD1FXCcSI5m0E8")

models = client.models.list()

for m in models:
    print(m.name)