import json
import requests

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body= { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = body, headers = headers)
    if response.status_code == 400:
        return {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}
    json_response = json.loads(response.text)
    result = json_response["emotionPredictions"][0]["emotion"]
    maxScore = 0
    maxEmotion = None 
    for emotion in result:
        if result[emotion] > maxScore: 
            maxScore = result[emotion]
            maxEmotion = emotion
    result["dominant_emotion"] = maxEmotion
    return result