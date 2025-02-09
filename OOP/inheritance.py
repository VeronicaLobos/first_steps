
"""
Car is the 'Parent class' or 'Superclass'.
Any variables and methods contained in it will
be inherited by a 'Child class' (also called
'Subclass' or "Derived class'.
"""

class Car:
    """
    A Car superclass stores and shows the miles driven.
    Instantiated cars have driven 0 miles.
    """
    def __init__(self):
        self.odometer = 0

    def drive(self, miles):
        """
        Is given a distance in miles and will update
        the odometer of the instance by adding it.
        """
        distance = miles
        self.odometer = self.odometer + distance

    def show_odometer(self):
        """
        Prints the miles driven by the Car instance.
        """
        print(f"Odometer: {self.odometer} miles traveled.")


"""
The following subclasses will copy Car's blueprint,
and implement an instance variable to store fuel/energy capacity.
The method drive is overriden to calculate the consumption rate
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
        self.fuel = gallons  # 20 - 60gal
        self.odometer = 0

    def drive(self, miles):
        """
        Overrides the ihherited instance method.
        This car consumes 0.08 galons for every mile.
        """
        fuel_consumed = miles * GasCar.CONSUMPTION_RATE
        self.fuel -= fuel_consumed
        self.odometer += miles

    def show_fuel_tank(self):
        """
        Prints the amount of gallons left in the fuel tank.
        """
        print(f"Fuel tank: {self.fuel} gallon(s) left.")

    def fill_tank(self, galons: int):
        """
        Fills the fuel tank.
        """
        self.fuel += galons
        print(f"Car refilled with {galons} galon(s).")


class ElectricCar(Car):
    """
    This subclass represents a Car that consumes
    electricity as a fuel resource to drive, and
    is measured in kilowatts per hour (kWh).
    """
    CONSUMPTION_RATE = 0.2

    def __init__(self, kwh):
        self.battery = kwh  # 20.000 - 140.000 kwh
        self.odometer = 0

    def drive(self, miles):
        """
        Overrides the ihherited instance method.
        This car consumes 0.2 kwh for every mile.
        """
        energy_consumed = miles * ElectricCar.CONSUMPTION_RATE
        self.battery -= ElectricCar.CONSUMPTION_RATE
        self.odometer += miles

    def show_battery(self):
        """
        Prints the amount of kwh left in the battery.
        """
        print(f"Battery: {self.battery} kwh(s) left.")

    def charge_battery(self, hours):
        """
        Fills the fuel tank.
        """
        electric_power = 8  # kw
        charge = electric_power * hours
        self.battery += charge  # kwh
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
