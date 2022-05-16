from silver_service_taxi import SilverServiceTaxi

def main():
    Silver_Taxi = SilverServiceTaxi("S Taxi", 100, 10)

    Silver_Taxi.drive(20)
    print(Silver_Taxi)

    print("\n")
    print(Silver_Taxi.get_fare())


if __name__ == "__main__":
    main()