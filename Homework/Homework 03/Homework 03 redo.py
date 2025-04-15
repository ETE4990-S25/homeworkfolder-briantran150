#going to create a file with dataclasses

from dataclasses import dataclass, asdict

@dataclass
class Person:
    name: str
    age: int
    email: str

@dataclass
class Student(Person):
    student_identification: str

#import my jsom function
import json
from typing import List

def save_to_json(filepath: str, objects: List[object]):
    with open(filepath, 'w') as f:
        json.dump([asdict(obj) for obj in objects], f, indent=2)

def display_json(filepath: str):
    with open(filepath, 'r') as f:
        data = json.load(f)
        print("\n Loaded JSON Data:")
        print(json.dumps(data, indent=2))

#time to test file

def main():

    King = Person(name="Lebron", age=40, email="LebronJames23@lakers.com")
    Rookie = Student(name="Brian", age=25, email="Briantherook@cpp.edu", student_identification="123456")

    save_to_json("people_data.json", [King, Rookie])

    display_json("people_data.json")

if __name__ == "__main__":
    main()

    





