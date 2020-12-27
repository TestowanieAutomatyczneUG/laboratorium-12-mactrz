from src.Subscriber import Subscriber
import unittest
from unittest.mock import MagicMock, Mock
from assertpy import assert_that

class TestSubscriber(unittest.TestCase):

    def setUp(self):
        self.tmp = Subscriber(['Person1'])

    def test_creation_exception(self):
        assert_that(Subscriber).raises(Exception).when_called_with('test').is_equal_to('Must be a list')

    def test_add(self):
        self.tmp.people = MagicMock()
        result = self.tmp.add('Person')
        assert_that(result).is_equal_to(True)

    def test_delete_exception(self):
        assert_that(self.tmp.delete).raises(Exception).when_called_with('Person2').is_equal_to('This person does not exist!')

    def test_delete(self):
        result = self.tmp.delete('Person1')
        assert_that(result).is_equal_to(True)

    def test_sendMessage_exception(self):
        assert_that(self.tmp.sendMessage).raises(Exception).when_called_with('Person2', 'Message').is_equal_to('This person does not exist!')

    def test_sendMessage(self):
        self.tmp.send = MagicMock()
        result = self.tmp.sendMessage('Person1', 'Message')
        assert_that(result).is_equal_to(True)