import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Check for blank input
    if not text_to_analyse.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the emotion analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion analysis API
    response = requests.post(url, json=myobj, headers=header, timeout=10)

    # Checking if the request was successful
    if response.status_code == 200:
        # Converting the JSON response into a Python dictionary
        formatted_response = json.loads(response.text)
        # Extracting the required set of emotions and their scores
        emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
        anger = emotion_predictions.get('anger', 0)
        disgust = emotion_predictions.get('disgust', 0)
        fear = emotion_predictions.get('fear', 0)
        joy = emotion_predictions.get('joy', 0)
        sadness = emotion_predictions.get('sadness', 0)
        # Finding the dominant emotion
        emotions = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness}
        dominant_emotion = max(emotions, key=emotions.get)
    elif response.status_code == 400:
        # Handling blank input with status code 400
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        # Setting default values in case of an error
        anger = disgust = fear = joy = sadness = 0
        dominant_emotion = None

    # Returning the emotions and the dominant emotion in the required format
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
