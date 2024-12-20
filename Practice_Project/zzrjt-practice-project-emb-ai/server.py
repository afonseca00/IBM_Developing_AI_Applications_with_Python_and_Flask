"""
Servidor Flask para Análise de Sentimento.
"""

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/")
def render_index_page():
    """
    Renderiza a página inicial.
    """
    return render_template("index.html")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """
    Analisa o texto recebido e retorna o rótulo e a pontuação de sentimento.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']
    if not text_to_analyze.strip():
        return "Input is blank! Please enter some text."
    if label is None:
        return "Invalid input! Try again."
    return f"The given text has been identified as {label.split('_')[1]} with a score of {score}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
