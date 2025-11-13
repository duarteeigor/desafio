from transformers import pipeline

def classify_email(text):
    text = text.lower()
    keywords_productive = ['ajuda', 'suporte', 'erro', 'problema', 'solicitação', 'atualização', 'cliente']
    keywords_unproductive = ['feliz natal', 'parabéns', 'obrigado', 'boa sorte', 'felicitações']

    count_prod = sum(1 for kw in keywords_productive if kw in text)
    count_unprod = sum(1 for kw in keywords_unproductive if kw in text)

    if count_prod > count_unprod:
        return "Produtivo"
    elif count_unprod > count_prod:
        return "Improdutivo"
    else:
        # Se empate, usar modelo pré-treinado para decidir
        
        classifier = pipeline("text-classification", model="lucsaa/classificador-de-emails")
        result = classifier(text[:512])
        label = result[0]['label']
        print(result[0]['label'])

        return "Produtivo" if label == 'POSITIVE' else "Improdutivo"
