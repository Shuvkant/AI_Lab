from datetime import datetime


class Person():
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def print_details(self):
        print(f"Name= {self.name} \nCountry={
              self.country}\nDate of birth= {self.dob}")

    def calculateAge(self):
        today = datetime.now().year
        age = today-self.dob
        print(f"Age= {age}")


person1 = Person("ram", "America", 2003)
person1.print_details()
person1.calculateAge()
