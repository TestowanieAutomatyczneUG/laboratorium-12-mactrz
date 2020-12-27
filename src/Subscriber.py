class Subscriber:

    def __init__(self, people=None):

        if people is None:
            people = []

        if type(people) != list:
            raise TypeError('Must be a list')
        self.people = people
        self.send = None

    def add(self, person):
        self.people.append(person)
        return True

    def delete(self, person):
        if person not in self.people:
            raise Exception('This person does not exist!')

        self.people.remove(person)
        return True

    def sendMessage(self, person, message):
        if person not in self.people:
            raise Exception('This person does not exist!')

        self.send(person, message)
        return True
