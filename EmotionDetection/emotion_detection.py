import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=input_json, headers=headers, timeout=30)
    
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotion_json = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotion_json['anger']
        disgust_score = emotion_json['disgust']
        fear_score = emotion_json['fear']
        joy_score = emotion_json['joy']
        sadness_score = emotion_json['sadness']
        dominant_emotion = max(emotion_json, key=lambda k: emotion_json[k])
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
    
    return {'anger': anger_score,'disgust': disgust_score,
'fear': fear_score,
'joy': joy_score,
'sadness': sadness_score,
'dominant_emotion': dominant_emotion
}