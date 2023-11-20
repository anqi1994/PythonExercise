class Hobby:
    def __init__(self, name, description, equipment):
        self.name = name
        self.description = description
        self.equipment = equipment
        self.participants = []


class Event:
    def __init__(self, name, location, date):
        self.name = name
        self.location = location
        self.date = date
        self.participants = []


class Citizen:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.hobbies = []
        self.events = []
        self.social = []


class SignUp:
    def __init__(self, citizen, target, category):
        self.citizen = citizen
        self.target = target
        self.category = category

        getattr(citizen, f'{category}s').append(self)






