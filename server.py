"""
    My Flask App for Emotion Detection.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector as ed


app = Flask("Emotion Detection App")

@app.route("/emotionDetector")
def detect_emotion():
    """
        Processes request from API call. Uses request parameter 'textToAnalyze'
        to run emotion detection on IBM Cloud
    """
    text_to_analyze = request.args.get("textToAnalyze")
    emotions = ed(text_to_analyze)
    output_string = "For the given statement, the system response is "
    for key in emotions:
        if key == "dominant_emotion":
            if emotions[key] is None :
                return "Invalid text! Please Try Again!"
            output_string += f". The dominant emotion is {emotions[key]}"
        else:
            output_string += f"'{key}': {emotions[key]}, "
    return output_string

@app.route("/")
def render_index():
    """
        Renders the website template
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "localhost", port = 5000)
