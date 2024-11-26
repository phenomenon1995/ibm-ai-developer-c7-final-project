"""
    Module for emotion detection
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
        Sends text to IBM cloud emotion detection API and returns a dictionary of
        emotions with their scores as well as the dominant emotion.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body= { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = body, headers = headers)
    if response.status_code == 400:
        return {"anger": None, "disgust": None, "fear": None,
         "joy": None, "sadness": None, "dominant_emotion": None}
    json_response = json.loads(response.text)
    result = json_response["emotionPredictions"][0]["emotion"]
    max_score = 0
    max_emotion = None
    for emotion in result:
        if result[emotion] > max_score:
            max_score = result[emotion]
            max_emotion = emotion

    result["dominant_emotion"] = max_emotion
    return result
