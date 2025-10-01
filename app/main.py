class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]
    for person_data in people:
        person_obj = Person.people[person_data["name"]]
        if "wife" in person_data and person_data["wife"] is not None:
            person_obj.wife = Person.people[person_data["wife"]]
        if "husband" in person_data and person_data["husband"] is not None:
            person_obj.husband = Person.people[person_data["husband"]]
    return persons
