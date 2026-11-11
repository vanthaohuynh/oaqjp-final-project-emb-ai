# Import the function we want to test, from our package
from EmotionDetection.emotion_detection import emotion_detector

# Import built-in Python testing library
import unittest

# Create a test class (a group of tests)
class TestEmotionDetector(unittest.TestCase):

    # The test functions, testing each case of emotion:
    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result['dominant_emotion'], 'fear')

# Run the test when this file is executed
unittest.main()
