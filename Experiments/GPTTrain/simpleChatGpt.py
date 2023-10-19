import requests

# Define la URL del API y el key
url = 'https://api.chatgpt.com/ask'
api_key = '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'

# Lee el archivo PDF
with open('docs/2020-Scrum-Guide-Spanish-European.pdf', 'rb') as file:
    pdf_data = file.read()

# Define los parámetros de la solicitud HTTP
payload = {
    'question': '¿Qué es COBIT y qué no es?',
    'context': pdf_data,
    'api_key': api_key
}

# Envía la solicitud HTTP
response = requests.post(url, json=payload)

# Procesa la respuesta del servidor
if response.status_code == 200:
    answer = response.json()['answer']
    print(answer)
else:
    print('Error al enviar la solicitud HTTP')