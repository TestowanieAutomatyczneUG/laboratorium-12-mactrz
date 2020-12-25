from unittest.mock import MagicMock
import unittest
from assertpy import assert_that
from src.APICall import APICall
import requests


class TestAPICallMock(unittest.TestCase):

    def setUp(self):
        self.tmp = APICall()
        self.values = {
            "results": [
                {
                    "gender": "male",
                    "name": {
                        "title": "mr",
                        "first": "brad",
                        "last": "gibson"
                    },
                    "location": {
                        "street": "9278 new road",
                        "city": "kilcoole",
                        "state": "waterford",
                        "postcode": "93027",
                        "coordinates": {
                            "latitude": "20.9267",
                            "longitude": "-7.9310"
                        },
                        "timezone": {
                            "offset": "-3:30",
                            "description": "Newfoundland"
                        }
                    },
                    "email": "brad.gibson@example.com",
                    "login": {
                        "uuid": "155e77ee-ba6d-486f-95ce-0e0c0fb4b919",
                        "username": "silverswan131",
                        "password": "firewall",
                        "salt": "TQA1Gz7x",
                        "md5": "dc523cb313b63dfe5be2140b0c05b3bc",
                        "sha1": "7a4aa07d1bedcc6bcf4b7f8856643492c191540d",
                        "sha256": "74364e96174afa7d17ee52dd2c9c7a4651fe1254f471a78bda0190135dcd3480"
                    },
                    "dob": {
                        "date": "1993-07-20T09:44:18.674Z",
                        "age": 26
                    },
                    "registered": {
                        "date": "2002-05-21T10:59:49.966Z",
                        "age": 17
                    },
                    "phone": "011-962-7516",
                    "cell": "081-454-0666",
                    "id": {
                        "name": "PPS",
                        "value": "0390511T"
                    },
                    "picture": {
                        "large": "https://randomuser.me/api/portraits/men/75.jpg",
                        "medium": "https://randomuser.me/api/portraits/med/men/75.jpg",
                        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/75.jpg"
                    },
                    "nat": "IE"
                }
            ],
            "info": {
                "seed": "fea8be3e64777240",
                "results": 1,
                "page": 1,
                "version": "1.3"
            }
        }

    def test_APICall_length(self):
        requests.get.json = MagicMock()
        requests.get.json.return_value = self.values
        result = self.tmp.request()
        assert_that(result['results']).is_length(1)

    def test_APICall_instance(self):
        requests.get.json = MagicMock()
        requests.get.json.return_value = self.values
        result = self.tmp.request()
        assert_that(result['results'][0]).is_instance_of(dict)

    def test_APICall_contains_email(self):
        requests.get.json = MagicMock()
        requests.get.json.return_value = self.values
        result = self.tmp.request()
        assert_that(result['results'][0]).contains_key('email')

    def test_APICall_login_length(self):
        requests.get.json = MagicMock()
        requests.get.json.return_value = self.values
        result = self.tmp.request()
        assert_that(result['results'][0]['login']).is_length(7)

    def test_APICall_age_type(self):
        requests.get.json = MagicMock()
        requests.get.json.return_value = self.values
        result = self.tmp.request()
        assert_that(result['results'][0]['dob']['age']).is_type_of(int)

    def test_APICall_many_length(self):
        requests.get.json = MagicMock()
        requests.get.json.return_value = {'results': [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}]}
        result = self.tmp.requestMany(10)
        assert_that(result['results']).is_length(10)

    def test_APICall_many_checkone(self):
        requests.get.json = MagicMock()
        requests.get.json.return_value = {'results': [{}, {}, {'dob': 'val'}, {}, {}, {}, {}, {}, {}, {}]}
        result = self.tmp.requestMany(10)
        assert_that(result['results'][2]).contains_key('dob')

    def test_APICall_many_exception_wrong_type(self):
        assert_that(self.tmp.requestMany).raises(TypeError).when_called_with('test').is_equal_to('Must be an integer')

    def test_APICall_gender_exception_type(self):
        assert_that(self.tmp.requestGender).raises(TypeError).when_called_with(1).is_equal_to('Gender must be a string')

    def test_APICall_gender_exception_value(self):
        assert_that(self.tmp.requestGender).raises(ValueError).when_called_with('kek').is_equal_to(
            'Must be either male or female')

    def test_APICall_gender_check_gender(self):
        requests.get.json = MagicMock()
        requests.get.json.return_value = self.values
        result = self.tmp.requestGender('male')
        assert_that(result['results'][0]['gender']).is_equal_to('male')

    def test_APICall_gender_check_gender_female(self):
        requests.get.json = MagicMock()
        self.values['results'][0]['gender'] = 'female'
        requests.get.json.return_value = self.values
        result = self.tmp.requestGender('female')
        assert_that(result['results'][0]['gender']).is_equal_to('female')

    def test_APICall_seed_exception_type(self):
        assert_that(self.tmp.requestSeed).raises(TypeError).when_called_with(1).is_equal_to('Seed must be a string')

    def test_APICall_seed_diff(self):
        requests.get.json = MagicMock()
        requests.get.json.return_value = self.values
        result1 = self.tmp.requestSeed('kek')

        self.values['results'][0]['gender'] = 'female'
        requests.get.json.return_value = self.values
        result2 = self.tmp.requestSeed('kek2')

        assert_that(result1).is_not_equal_to(result2)

    def test_APICall_seed_same(self):
        requests.get.json = MagicMock()
        requests.get.json.return_value = self.values
        result1 = self.tmp.requestSeed('kek')
        result2 = self.tmp.requestSeed('kek')

        assert_that(result1).is_equal_to(result2)
