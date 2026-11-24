"""Emotion detection module"""

import json
import requests

API_BASE_URL = "https://sn-watson-emotion.labs.skills.network"
MODEL = "emotion_aggregated-workflow_lang_en_stock"

def emotion_detector(text_to_analyze: str) -> dict:
    """This function detect emotions in a given text."""

    url = API_BASE_URL + "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": MODEL}
    data = {"raw_document": { "text": text_to_analyze }}
    response: requests.Response = requests.post(
        url=url,
        headers=headers,
        json=data,
        timeout=5
    )

    emotions: dict[str, float|None] = {}
    dominant_emotion: str = ""

    if response.status_code == 200:
        serialized_response: dict = json.loads(response.text)
        emotions = serialized_response["emotionPredictions"][0]["emotion"]
        dominant_emotion = next (
            emotion for emotion, score in emotions.items()
            if score == max(emotions.values())
        )
    elif response.status_code == 400:
        for k in ("anger", "fear", "disgust", "sadness", "joy"):
            emotions[k] = None
        dominant_emotion = None

    detection_result = {**emotions, "dominant_emotion": dominant_emotion}
    return detection_result
