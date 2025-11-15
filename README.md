# Documentação do Projeto Flask de Classificação de E-mails

## 1. Visão Geral

Este projeto consiste em uma aplicação web desenvolvida em **Flask** que recebe um texto de e-mail enviado pelo usuário, processa esse texto, classifica a categoria do e-mail e gera uma resposta automática sugerida com base nessa classificação.

A aplicação é composta pelos seguintes componentes principais:

* **app.py** – arquivo principal contendo rotas Flask e integração entre processamento, classificação e geração de resposta.
* **text_processing.py** – módulo responsável por pré-processar o texto.
* **classifier.py** – módulo responsável por classificar o texto em categorias.
* **generated_response.py** – módulo que gera uma resposta automática baseada no texto e na categoria.

---

## 2. Estrutura do Arquivo `app.py`

### 2.1. Importações

```python
from flask import Flask, render_template, request
from text_processing import processText
from classifier import classify_email
from generated_response import gerar_resposta_api
```

Essas importações permitem:

* Criar rotas e renderizar páginas HTML (Flask).
* Processar texto recebido.
* Classificar a categoria do e-mail.
* Gerar uma resposta automática.

---

## 3. Inicialização da Aplicação Flask

```python
app = Flask(__name__)
```

Cria a instância principal da aplicação.

---

## 4. Rotas

### 4.1. Rota Principal (`/`)

```python
@app.route('/')
def index():
    return render_template('index.html')
```

* Retorna a página inicial da aplicação.
* Renderiza o arquivo `index.html` que contém o formulário para envio do texto.

---

### 4.2. Rota de Análise (`/analisar`)

```python
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
```

#### Etapas executadas:

1. **Recebe o texto do formulário HTML**.
2. **Valida** se o texto não está vazio.
3. **Processa o texto** usando `processText()`.
4. **Classifica o e-mail** usando `classify_email()`.
5. **Gera uma resposta automática** com `gerar_resposta_api()`.
6. **Retorna para o usuário** a categoria identificada e a resposta sugerida.

---

## 5. Execução Local

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Permite rodar a aplicação localmente com debug habilitado.

---

## 6. Integração com AWS Lambda

```python
def handler(event, context):
    return app(event, context)
```

* Função handler que adapta a aplicação para ambientes serverless.
* Permite integração com **AWS API Gateway + Lambda**.

---

## 7. Fluxo Completo da Aplicação

1. Usuário acessa a página inicial.
2. Envia um texto para análise.
3. O texto é pré-processado.
4. O texto processado é classificado.
5. A API interna gera uma resposta automática.
6. Usuário recebe a categoria e a resposta sugerida.

---

## 8. Arquitetura Lógica

```
[Usuário] → [Formulário HTML] → [Flask /analisar] →
→ processText → classify_email → gerar_resposta_api →
→ [Resposta ao usuário]
```

---

