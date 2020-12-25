import requests

class APICall:

    def request(self):
        r = requests.get('https://randomuser.me/api/').json()
        return r

    def requestMany(self, results):
        if type(results) != int:
            raise TypeError('Must be an integer')

        r = requests.get('https://randomuser.me/api/?results={}'.format(results)).json()
        return r

    def requestGender(self, gender):
        if type(gender) != str:
            raise TypeError('Gender must be a string')

        if gender != 'male' and gender != 'female':
            raise ValueError('Must be either male or female')

        r = requests.get('https://randomuser.me/api/?gender={}'.format(gender)).json()
        return r

    def requestSeed(self, seed):
        if type(seed) != str:
            raise TypeError('Seed must be a string')

        r = requests.get('https://randomuser.me/api/?seed={}'.format(seed)).json()
        return r