from EmotionDetection.emotion_detection import emotion_detector as ed
from flask import Flask, render_template, request

app = Flask("Emotion Detection App")

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze")
    emotions = ed(text_to_analyze)
    output_string = "For the given statement, the system response is "
    for key in emotions:
        if key == "dominant_emotion":
            if emotions[key] == None : return "Invalid text! Please Try Again!"
            output_string += ". The dominant emotion is {}".format(emotions[key])
        else:
            output_string += "'{}': {}, ".format(key, emotions[key])
    return output_string

@app.route("/")
def render_index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "localhost", port = 5000)