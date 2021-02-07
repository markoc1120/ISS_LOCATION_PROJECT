import requests
import math


class Data:

    def __init__(self):
        self.response = requests.get("http://api.open-notify.org/iss-now.json")
        self.response.raise_for_status()
        self.long = self.response.json()["iss_position"]["longitude"]
        self.lat = self.response.json()["iss_position"]["latitude"]
        self.x = (180 + float(self.long)) * (1280 / 360)
        self.y = (90 - float(self.lat)) * (640 / 180)
        self.older = [self.x, self.y]
        self.rotation = 0
        self.older_rotation = 0

    def get_position(self):
        self.response = requests.get("http://api.open-notify.org/iss-now.json")
        self.response.raise_for_status()
        self.long = self.response.json()["iss_position"]["longitude"]
        self.lat = self.response.json()["iss_position"]["latitude"]
        self.x = (180 + float(self.long)) * (1280 / 360)
        self.y = (90 - float(self.lat)) * (640 / 180)

        if self.y < self.older[1]:
            self.rotation = math.atan((self.x - self.older[0]) / (self.older[1] - self.y))
        else:
            self.rotation = math.atan((self.y - self.older[1]) / (self.x - self.older[0]))

        if self.older_rotation == 0:
            self.older_rotation = self.rotation
