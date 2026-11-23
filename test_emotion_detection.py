import unittest

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def test_can_detect_anger(self) -> None:
        self._test_emotion(
            emotion="anger",
            text="I am really mad about this"
        )

    def test_can_detect_disgust(self) -> None:
        self._test_emotion(
            emotion="disgust",
            text="I feel disgusted just hearing about this"
        )

    def test_can_detect_fear(self) -> None:
       self._test_emotion(
        emotion="fear",
        text="I am really afraid that this will happen"
       )

    def test_can_detect_joy(self) -> None:
        self._test_emotion(
            emotion="joy",
            text="I am glad this happened"
        )

    def test_can_detect_sadness(self) -> None:
        self._test_emotion(
            emotion="sadness",
            text="I am so sad about this"
        )

    def _test_emotion(self, emotion: str, text: str) -> None:
        detection_result: dict = emotion_detector(text)
        
        self._test_output_format(detection_result)
        self.assertEqual(detection_result.get("dominant_emotion"), emotion)
        self.assertEqual(detection_result.get(emotion), max(list(detection_result.values())[:-1]))

    def _test_output_format(self, output) -> None:
        self.assertIsInstance(output, dict)
        self.assertEqual(len(output), 6)
        self.assertIn("anger", output)
        self.assertIn("fear", output)
        self.assertIn("disgust", output)
        self.assertIn("sadness", output)
        self.assertIn("joy", output)
        self.assertIn("dominant_emotion", output)

if __name__ == "__main__":
    unittest.main()