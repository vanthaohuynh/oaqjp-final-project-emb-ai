"""
Flask web server for the Emotion Detection application.
It receives text from the web page, analyzes it with Watson NLP,
and returns the emotion scores and the dominant emotion.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the text sent by the web page and return the emotion
    scores and the dominant emotion as a readable sentence.
    Return an error message if the input is blank or invalid.
    """
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

    # NEW: blank or invalid input -> show an error message
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Build the return in the format being requested:
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """Render the main page of the application."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
