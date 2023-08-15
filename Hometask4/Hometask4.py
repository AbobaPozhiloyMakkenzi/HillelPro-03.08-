import random
import string

used_plates = set()


class CarComponents:
    def numbers_for_cars(self):
        while True:
            num = random.randrange(1, 9999, 4)
            yield num

    def area_determiner(self):
        plates_dict = {
            "Dnipro": ["AE", "KE"],
            "Kyiv": ["AA", "KA"],
            "Odessa": ["Vn", "NN"],
            "Lviv": ["VS", "NS"],
            "Donetsk": ["AN", "KN"],
            "Kharkiv": ["AX"],
        }
        location = input("Where are you from")
        if location.capitalize() in plates_dict.keys():
            res1 = plates_dict.get(f"{location}")
            return random.choice(res1)
        else:
            print("Your location is not available now :( ")
            return None

    def seria_number(self):
        while True:
            res = "".join(random.choices(string.ascii_uppercase, k=2))
            yield res


Car = CarComponents()


class CarGenerator:
    def __init__(self, x, y, z):
        self.x = str(x)
        self.y = str(y)
        self.z = str(z)

    def __str__(self):
        res = str(f"{self.x}{self.y}{self.z}")
        return res


def construct():
    while True:
        ready_plate = CarGenerator(
            Car.area_determiner(),
            next(Car.numbers_for_cars()),
            next(Car.seria_number()),
        )
        if ready_plate in used_plates:
            print("Please, regenerate a plate!")
            construct()
        elif str(ready_plate).startswith("None"):
            print("try again")
            construct()
        else:
            used_plates.add(ready_plate)
            yield ready_plate


if __name__ == "__main__":
    print(next(construct()))