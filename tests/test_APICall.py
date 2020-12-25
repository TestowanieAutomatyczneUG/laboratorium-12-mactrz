from src.APICall import APICall
import unittest
from assertpy import assert_that

class TestAPICall(unittest.TestCase):

    def setUp(self):
        self.tmp = APICall()

    def test_APICall_length(self):
        result = self.tmp.request()
        assert_that(result['results']).is_length(1)

    def test_APICall_instance(self):
        result = self.tmp.request()
        assert_that(result['results'][0]).is_instance_of(dict)

    def test_APICall_contains_email(self):
        result = self.tmp.request()
        assert_that(result['results'][0]).contains_key('email')

    def test_APICall_login_length(self):
        result = self.tmp.request()
        assert_that(result['results'][0]['login']).is_length(7)

    def test_APICall_age_type(self):
        result = self.tmp.request()
        assert_that(result['results'][0]['dob']['age']).is_type_of(int)

    def test_APICall_many_length(self):
        result = self.tmp.requestMany(10)
        assert_that(result['results']).is_length(10)

    def test_APICall_many_checkone(self):
        result = self.tmp.requestMany(10)
        assert_that(result['results'][2]).contains_key('dob')

    def test_APICall_many_exception_wrong_type(self):
        assert_that(self.tmp.requestMany).raises(TypeError).when_called_with('test').is_equal_to('Must be an integer')

    def test_APICall_gender_exception_type(self):
        assert_that(self.tmp.requestGender).raises(TypeError).when_called_with(1).is_equal_to('Gender must be a string')

    def test_APICall_gender_exception_value(self):
        assert_that(self.tmp.requestGender).raises(ValueError).when_called_with('kek').is_equal_to('Must be either male or female')

    def test_APICall_gender_check_gender(self):
        result = self.tmp.requestGender('male')
        assert_that(result['results'][0]['gender']).is_equal_to('male')

    def test_APICall_seed_exception_type(self):
        assert_that(self.tmp.requestSeed).raises(TypeError).when_called_with(1).is_equal_to('Seed must be a string')

    def test_APICall_seed(self):
        result1 = self.tmp.requestSeed('kek')
        result2 = self.tmp.requestSeed('kek')

        assert_that(result1).is_equal_to(result2)
