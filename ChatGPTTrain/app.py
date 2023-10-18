# app.py

from flask import Flask, render_template, request, jsonify
import PyPDF2
import openai

app = Flask(__name__)

# Configure OpenAI API
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"})

    if file:
        pdf_text = extract_text_from_pdf(file)
        return jsonify({"text": pdf_text})

@app.route("/ask", methods=["POST"])
def ask():
    pdf_text = request.json.get("pdf_text")
    question = request.json.get("question")
    answer = generate_answer(pdf_text, question)
    return jsonify({"answer": answer})

def extract_text_from_pdf(file):
    pdf_text = ""
    try:
        pdf_reader = PyPDF2.PdfFileReader(file)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_text += page.extractText()
        return pdf_text
    except Exception as e:
        return str(e)

def generate_answer(pdf_text, question):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Read the following text and answer the question:\n\n{pdf_text}\n\nQuestion: {question}\nAnswer:",
            max_tokens=50,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
