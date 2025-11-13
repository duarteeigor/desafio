from flask import Flask, render_template, request
from text_processing import  processText
from classifier import classify_email
from generated_response import gerar_resposta_api


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

# if __name__ == "__main__":
#     app.run()

def handler(event, context):
    return app(event, context)



