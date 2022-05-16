from prac_08.taxi import Taxi

def main():

    # Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
    new_taxi = Taxi('Prius 1', 100)
    # Drive the taxi 40 km
    new_taxi.drive(40)
    # Print the taxi's details and the current fare
    print(new_taxi)
    print(f"--Current fare: ${new_taxi.get_fare():.2f}")
    # Restart the meter (start a new fare) and then drive the car 100 km
    new_taxi.start_fare()
    new_taxi.drive(100)
    # Print the details and the current fare
    print(new_taxi)


if __name__ == "__main__":
    main()