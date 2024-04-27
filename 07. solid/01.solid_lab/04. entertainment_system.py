from abc import ABC, abstractmethod


class Cable(ABC):
    @abstractmethod
    def connect(self, d1, d2):
        pass


class HDMICable(Cable):
    def connect(self, device1, device2):
        return f"Connect {device1} to {device2} via HDMI"


class RCACable(Cable):
    def connect(self, device1, device2):
        return f"Connect {device1} to {device2} via RCA"


class EthernetCable(Cable):
    def connect(self, device1, device2):
        return f"Connect {device1} to {device2} via Ethernet"


class Device:
    def __init__(self, model):
        self.model = model

    def connect_to_power(self):
        return "Shut down battery consumption, increase brightness "


class Television:
    pass


class DVDPlayer:
    pass


class GameConsole:
    pass


class Router:
    pass


hdmi = HDMICable()
tv = Television()
gc = GameConsole()

hdmi.connect(tv, gc)
