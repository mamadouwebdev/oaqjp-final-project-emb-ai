from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.get("/")
@app.get("/home")
@app.get("/index")
def get_home_page():
    return render_template("index.html")

@app.get("/emotionDetector")
def detect_emotion() -> dict:
    text = request.args.get("textToAnalyze")
    detection_result = emotion_detector(text)
    if detection_result["dominant_emotion"] == None:
        return "Invalid text! Please try again!"
    return detection_result

if __name__ == "__main__":
    app.run(port=5000)