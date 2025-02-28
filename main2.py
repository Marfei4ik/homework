import random
class cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_eat(self):
        print("Time to eat")
        self.progress += 0.12
        self.gladness -= 3


    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:+^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

lucky = cat(name="lucky")   #друзья кота
rex = cat(name="rex")
dimon = cat(name="dimon")
for day in range(3650):
    if lucky.alive == False:
        break
    lucky.live(day)
    if rex.alive == False:
        break
    rex.live(day)
    if dimon.alive == False:
        break
    dimon.live(day)