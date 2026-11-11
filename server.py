# Import Flask, render_template, request from the flask pramework package
# Import the sentiment_analyzer function from the package created
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    # Get the text the user typed (sent by mywebscript.js)
    text_to_analyze = request.args.get('textToAnalyze')
 
    # Analyze it with Watson
    response = emotion_detector(text_to_analyze)

    # Take each value from the result dictionary
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Build the return in the format being requested:
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    # Rendering the index page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
