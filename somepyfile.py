class User:
    def __init__(self, userID: int, name: str, age: int):
        self.userID = userID
        self.name = name
        self.age = age

    def Display(self):
        print("--------------------")
        print(f"user id: {self.userID}")
        print(f"user age: {self.age}")
        print(f"user name: {self.name}")
        print("--------------------")

tobi = User(22, 'Simon', 18)
tobi.Display()