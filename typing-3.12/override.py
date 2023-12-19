# pyright: strict
from abc import ABC, abstractmethod
from typing import override

class Vehicle(ABC):  # Abstract Base Class (~Interface)
    @abstractmethod
    #def refill(self):
    def energize(self):
        pass

class ElectricVehicle(Vehicle):
    @override
    def refill(self):
        ... # Charging logic

class InternalCombustionVehicle(Vehicle):
    @override
    def refill(self):
        ... # Refueling logic
