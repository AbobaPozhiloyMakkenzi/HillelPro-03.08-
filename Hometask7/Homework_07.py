import difflib
import logging
import random
import string
import time


class TimerContext:
    def __enter__(self):
        self.time_start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.running_time = time.time() - self.time_start
        logging.info(self.running_time)

    class CarComponents:
        def numbers_for_cars(self):
            while True:
                num = random.randrange(1, 9999, 4)
                yield num

        def area_determiner(self):
            plates_dict = {
                "Dnipro": ["AE", "KE"],
                "Kyiv": ["AA", "KA"],
                "Odessa": ["VN", "NN"],
                "Lviv": ["VS", "NS"],
                "Donetsk": ["AN", "KN"],
                "Kharkiv": ["AX"],
            }
            location = input("Where are you from").strip().capitalize()
            if location in plates_dict.keys():
                res1 = plates_dict.get(f"{location}")
                return random.choice(res1)
            elif location.capitalize() not in plates_dict.keys():
                probable_meaning = difflib.get_close_matches(
                    location, plates_dict.keys()
                )
                try:
                    quest = input(
                        f"Seems like you made a mistake, perhaps you meant {probable_meaning[0]}?"
                    ).strip()
                except Exception as e:
                    print(f"we are sorry, but your locatuon is not available yet!{e}")
                else:
                    if quest == "yes":
                        res1 = plates_dict.get(f"{probable_meaning[0]}")
                        return random.choice(res1)
                    else:
                        return None

        def seria_number(self):
            while True:
                res = "".join(random.choices(string.ascii_uppercase, k=2))
                yield res

    used_plates = set()
    Car = CarComponents()

    class CarGenerator:
        def __init__(self, x, y, z):
            self.x = str(x)
            self.y = str(y)
            self.z = str(z)

        def __str__(self):
            res = str(f"{self.x}{self.y}{self.z}")
            return res

    def construct(self):
        while True:
            ready_plate = self.CarGenerator(
                self.Car.area_determiner(),
                next(self.Car.numbers_for_cars()),
                next(self.Car.seria_number()),
            )
            if ready_plate in self.used_plates:
                print("Please, regenerate a plate!")
                self.construct()
            elif str(ready_plate).startswith("None"):
                print("try again")
                self.construct()
            else:
                self.used_plates.add(ready_plate)
                yield ready_plate


# Set up logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

with TimerContext() as my_time_context:
    res = my_time_context.construct()
    time.sleep(1)
    logging.info(next(res))
