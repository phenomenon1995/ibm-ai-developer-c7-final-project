from EmotionDetection.emotion_detection import emotion_detector as ed
import unittest


class TestEmotionDetection(unittest.TestCase):
    def test_dominant_emotions(self):
        TEST_STRINGS = {
        "I am glad this happened":"joy",
        "I am really mad about this":"anger",
        "I feel disgusted just hearing about this":"disgust",
        "I am so sad about this":"sadness",
        "I am really afraid that this will happen":	"fear"}
        for statement in TEST_STRINGS:
            self.assertEquals(ed(statement)["dominant_emotion"], TEST_STRINGS[statement])

if __name__ == "__main__":
    unittest.main()