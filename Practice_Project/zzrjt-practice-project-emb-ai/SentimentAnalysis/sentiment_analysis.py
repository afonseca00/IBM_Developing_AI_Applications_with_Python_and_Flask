"""
Módulo para Análise de Sentimento usando Watson NLP API
"""

import json
import requests

def sentiment_analyzer(text_to_analyse):
    """
    Analisa o sentimento do texto fornecido.

    Args:
        text_to_analyse (str): O texto a ser analisado.

    Returns:
        dict: Um dicionário contendo o rótulo e a pontuação do sentimento.
    """
    url = (
        'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/'
        'NlpService/SentimentPredict'
    )
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json=myobj, headers=header, timeout=10)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    else:
        label = None
        score = None

    return {'label': label, 'score': score}
