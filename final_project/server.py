"""
This module sets up a Flask web application to analyze emotions in text using the 
Watson NLP library.
"""

import os
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Define the path to the templates and static directories
template_dir = os.path.abspath('oaqjp-final-project-emb-ai/templates')
static_dir = os.path.abspath('oaqjp-final-project-emb-ai/static')

app = Flask("Emotion Detector", template_folder=template_dir, static_folder=static_dir)

@app.route("/")
def render_index_page():
    """
    Render the index page.

    Returns:
        str: Rendered HTML of the index page.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyze the provided text and return the emotions and the dominant emotion.

    Returns:
        str: Response string with emotions and dominant emotion or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (
        f"For the given statement, the system response is 'anger': {anger},"
        f"'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
