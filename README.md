📧 Email Classifier AI

Aplicação web que classifica emails automaticamente como Produtivos ou Improdutivos e gera uma resposta automática inteligente utilizando IA.

📌 Visão Geral

Este projeto foi desenvolvido para automatizar a triagem e resposta de emails dentro de uma grande empresa do setor financeiro, que recebe diariamente um alto volume de mensagens — algumas relevantes e outras completamente improdutivas.

A solução permite:

Upload ou inserção direta de texto de emails

Processamento de linguagem natural (NLP)

Classificação inteligente (Produtivo × Improdutivo)

Geração automática de respostas

Interface simples e funcional (Flask + HTML)

🚀 Tecnologias Utilizadas
Backend

Python 3.x

Flask

Biblioteca de NLP (stopwords, lematização, limpeza de texto)

API de IA para classificação e geração de respostas (ex.: GPT)

Frontend

HTML5

CSS básico

Formulário com textarea para envio do conteúdo do email

📂 Estrutura do Projeto
/meu-projeto
│── app.py
│── classifier.py
│── generated_response.py
│── text_processing.py
│── requirements.txt
│
└── /templates
    └── index.html

🧠 Funcionamento da Solução
1. Entrada do Usuário

O usuário acessa a página inicial (index.html) e insere o texto do email.

2. Pré-processamento

Arquivo: text_processing.py

Responsável por:

normalização do texto

remoção de stopwords

lematização (se implementado)

limpeza geral

Função principal usada:

formated = processText(email_text)

3. Classificação

Arquivo: classifier.py

Utiliza IA ou regras definidas para determinar a categoria:

Produtivo

Improdutivo

Função chamada:

category = classify_email(formated)

4. Geração da resposta

Arquivo: generated_response.py

Chama uma API de IA para gerar um texto coerente e adequado à categoria:

response = gerar_resposta_api(formated, category)

5. Retorno ao usuário

A aplicação retorna:

Categoria: Produtivo ou Improdutivo
Resposta sugerida: <texto gerado pela IA>

🖥️ Código Principal — app.py
from flask import Flask, render_template, request
from text_processing import processText
from classifier import classify_email
from generated_response import gerar_resposta_api

app = Flask(__name__)

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
    response = gerar_resposta_api(formated, category)

    print("Texto recebido: ", formated, category)
    return f"Categoria: {category}\nResposta sugerida: {response}"

if __name__ == "__main__":
    app.run(debug=True)

def handler(event, context):
    return app(event, context)

🌐 Execução Local
1. Instalar dependências
pip install -r requirements.txt

2. Rodar a aplicação
python app.py

3. Acessar o navegador
http://127.0.0.1:5000