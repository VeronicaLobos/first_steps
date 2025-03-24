from abc import ABC, abstractmethod


"""
Car is the 'Parent class' or 'Superclass'.
Any variables and methods contained in it will
be inherited by a 'Child class' (also called
'Subclass' or "Derived class'.
"""

class Car(ABC):
    """
    A Car superclass stores and shows the miles driven.
    Instantiated cars have driven 0 miles.
    """
    def __init__(self):
        self._odometer = 0

    @abstractmethod
    def drive(self, distance):
        """
        Is given a distance in miles and will update
        the odometer of the instance by adding it.
        """
        self._odometer = self._odometer + distance

    def show_odometer(self):
        """
        Prints the miles driven by the Car instance.
        """
        print(f"Odometer: {self._odometer} miles traveled.")


"""
The following subclasses will copy Car's blueprint,
and implement an instance variable to store fuel/energy capacity.
The method drive is overridden to calculate the consumption rate
based on the kind of combustible being used by the subclass.
"""

class GasCar(Car):
    """
    This subclass represents a Car that consumes
    gas as a fuel resource, and the value stored
    as fuel is measured in gallons.
    """
    CONSUMPTION_RATE = 0.08

    def __init__(self, gallons):
        """
        Odometer logic is maintained, behold abstraction!
        Fuel volume now required.
        """
        super().__init__()
        self.__fuel = gallons  # 20 - 60gal

    def drive(self, distance):
        """
        Overrides the inherited instance method.
        This car consumes 0.08 gallons for every mile.
        Updates odometer.
        """
        fuel_consumed = distance * GasCar.CONSUMPTION_RATE
        self.__fuel -= fuel_consumed
        super().drive(distance)

    def show_fuel_tank(self):
        """
        Prints the amount of gallons left in the fuel tank.
        """
        print(f"Fuel tank: {self.__fuel} gallon(s) left.")

    def fill_tank(self, gallons: int):
        """
        Fills the fuel tank.
        """
        self.__fuel += gallons
        print(f"Car refilled with {gallons} gallon(s).")


class ElectricCar(Car):
    """
    This subclass represents a Car that consumes
    electricity as a fuel resource to drive, and
    is measured in kilowatts per hour (kWh).
    """
    CONSUMPTION_RATE = 0.2

    def __init__(self, kwh):
        """
        Inherits the odometer instance value from Car.
        Battery charge required before driving.
        """
        super().__init__()
        self.__battery = kwh  # 20.000 - 140.000 kwh

    def drive(self, distance):
        """
        Overrides the ihherited instance method.
        This car consumes 0.2 kwh for every mile.
        Updates odometer.
        """
        energy_consumed = distance * ElectricCar.CONSUMPTION_RATE
        self.__battery -= energy_consumed
        super().drive(distance)

    def show_battery(self):
        """
        Prints the amount of kwh left in the battery.
        """
        print(f"Battery: {self.__battery} kwh(s) left.")

    def charge_battery(self, hours):
        """
        Fills the fuel tank.
        """
        electric_power = 8  # kw
        charge = electric_power * hours
        self.__battery += charge  # kwh
        print(f"Car charged for {hours} hour(s).")


def main():
    """
    Instantiates a Gas and an Electric car subclasses.
    Takes the car for a ride to see if it works,
    checks that the odometer reading is correct,
    checks that the fuel reading is correct after refueling.
    """
    volkswagen = GasCar(20)
    hyundai = ElectricCar(8)

    print("Let's test this Volkswagen:")
    volkswagen.show_fuel_tank()
    volkswagen.show_odometer()
    volkswagen.drive(125)
    volkswagen.show_fuel_tank()
    volkswagen.show_odometer()
    volkswagen.fill_tank(5)
    volkswagen.show_fuel_tank()

    print("\nLet's check this Hyundai:")
    hyundai.show_battery()
    hyundai.show_odometer()
    hyundai.drive(25)
    hyundai.show_battery()
    hyundai.show_odometer()
    hyundai.charge_battery(1)
    hyundai.show_battery()


if __name__ == "__main__":
    main()
