from flask import Flask, render_template, request
from api.text_processing import  processText
from api.classifier import classify_email
from api.generated_response import gerar_resposta_api


app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analisar', methods=['POST'])
def analisar():
    email_text = request.form['email']
    if not email_text.strip():
        return "Nenhuma mensagem enviada"
    
    formated = processText(email_text)
    category = classify_email(formated)
    response = gerar_resposta_api(formated)

    print("Texto recebido: ", formated, category)
    return f"Categoria: {category}\nResposta sugerida: {response}"

def handler(request, *args, **kwargs):
    return app(request.environ, request.start_response)



