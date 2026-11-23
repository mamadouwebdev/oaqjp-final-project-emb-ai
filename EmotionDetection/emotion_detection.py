import json
import requests

API_BASE_URL = "https://sn-watson-emotion.labs.skills.network"
MODEL = "emotion_aggregated-workflow_lang_en_stock"

def emotion_detector(text_to_analyze: str) -> dict:
    url = API_BASE_URL + "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": MODEL}
    data = {"raw_document": { "text": text_to_analyze }}
    
    response: requests.Response = requests.post(
        url=url,
        headers=headers,
        json=data
    )

    serialized_response: dict = json.loads(response.text)
    emotions: dict[str, float] = serialized_response["emotionPredictions"][0]["emotion"]

    emotions["dominant_emotion"]: str = next (
        emotion for emotion, score in emotions.items()
        if score == max(emotions.values())
    )
    return emotions
