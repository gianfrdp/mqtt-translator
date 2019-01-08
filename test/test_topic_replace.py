import unittest
from mqtt_translator.translator.topic_replace import TopicReplace
from paho.mqtt.client import MQTTMessage


class TestTopicReplace(unittest.TestCase):

    def test_translate_givenMatchingConfig_shouldTranslate(self):
        config = [
            {'from': 'xyz', 'to': '123'},
            {'from': 'home', 'to': 'away'}
        ]
        translator = TopicReplace(config)
        message = MQTTMessage()
        message.topic = 'home xyz'.encode('utf-8')

        translator.translate(message)

        self.assertEqual(message.topic, 'away 123')

    def test_translate_givenNotMatchingConfig_shouldNotTranslate(self):
        config = [
            {'from': 'xyz', 'to': '123'},
            {'from': 'home', 'to': 'away'}
        ]
        translator = TopicReplace(config)
        message = MQTTMessage()
        message.topic = 'baby G'.encode('utf-8')

        translator.translate(message)

        self.assertEqual(message.topic, 'baby G')

    def test_translate_givenTwoMatchingConfigs_shouldTranslateInOrder(self):
        config = [
            {'from': 'xyz', 'to': '123'},
            {'from': '123', 'to': 'zyx'}
        ]
        translator = TopicReplace(config)
        message = MQTTMessage()
        message.topic = 'xyz'.encode('utf-8')

        translator.translate(message)

        self.assertEqual(message.topic, 'zyx')


if __name__ == '__main__':
    unittest.main()
