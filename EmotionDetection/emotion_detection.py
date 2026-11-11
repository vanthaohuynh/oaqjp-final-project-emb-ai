import json      # Library to convert JSON text into a Python dictionary
import requests  # Library to send HTTP requests to the Watson service

def emotion_detector(text_to_analyze):
    # Address of the Watson Emotion Detection service
    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Header that tells Watson which AI model to use
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # The text we want analyzed, in the format Watson expects
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Send the request to Watson
    response = requests.post(url, json=myobj, headers=header)

    # NEW: blank input -> Watson answers with status code 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Convert Watson's text answer into a dictionary
    formatted_response = json.loads(response.text)

    # Go down to the 5 emotion scores:
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Separate each score
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Find the emotion with the highest score
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

