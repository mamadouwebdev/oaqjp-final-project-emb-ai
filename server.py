"""This module contain the server of the application"""

from flask import Flask, render_template, request

from emotion_detection import emotion_detector

app = Flask(__name__)

@app.get("/")
@app.get("/home")
@app.get("/index")
def get_home_page():
    "The endpoint of the home page."
    return render_template("index.html")

@app.get("/emotionDetector")
def detect_emotion() -> dict:
    """Emotion detection endpoint."""
    text = request.args.get("textToAnalyze")
    detection_result = emotion_detector(text)
    if detection_result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return detection_result

if __name__ == "__main__":
    app.run(port=5000)
