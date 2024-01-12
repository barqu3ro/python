import openai
import PyPDF2

# Configura tu API key de OpenAI
openai.api_key = 'TU_API_KEY'

# Lee el contenido del archivo PDF
def leer_pdf(ruta_archivo):
    with open(ruta_archivo, 'rb') as archivo:
        lector_pdf = PyPDF2.PdfFileReader(archivo)
        texto = ''
        for pagina in range(lector_pdf.numPages):
            texto += lector_pdf.getPage(pagina).extractText()
        return texto

# Conectarse al chat GPT y hacer preguntas
def hacer_preguntas(texto):
    respuesta = openai.Completion.create(
        engine='text-davinci-003',
        prompt=texto,
        max_tokens=100
    )
    return respuesta.choices[0].text.strip()

# Ruta del archivo PDF
ruta_pdf = 'docs/archivo.pdf'

# Leer el contenido del archivo PDF
contenido_pdf = leer_pdf(ruta_pdf)

# Hacer preguntas al chat GPT
respuesta_chat = hacer_preguntas(contenido_pdf)

print(respuesta_chat)
