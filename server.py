"""
This module defines a Flask application for emotion detection.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the index template."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """Process the textToAnalyze parameter and return the emotion detection result."""
    statement = request.args.get('textToAnalyze')
    result = emotion_detector(statement)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    response_str = (
        f"For the given statement, the system response is: "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_str

if __name__ == "__main__":
    app.run(debug=True)
