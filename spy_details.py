# importing date and time
from datetime import datetime

# using class and name spy
class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

# making class chat message for reading
class chatmessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('ABCD', 'Mr.', 24, 2)

friend_one = Spy('Sumit', 'Mr.', 3, 27)
friend_two = Spy('Dubbs', 'Mr.', 4, 21)
friend_three = Spy('Aku', 'Mr.', 4.5, 37)


friends = [friend_one, friend_two, friend_three]
