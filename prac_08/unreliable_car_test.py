from prac_08.unreliable_car import UnreliableCar

def main():

    # initialize 2 car
    CarA = UnreliableCar("CarA",100,95)
    CarB = UnreliableCar("CarB",100,10)

    # run 10 test
    for i in range(1,10):
        print("-----Car Test-----")
        print("{:8} drove {:2}km".format(CarA.name, CarA.drive(i)))
        print("{:8} drove {:2}km".format(CarB.name, CarB.drive(i)))

    # print the result of cars
    print(CarA)
    print(CarB)


if __name__ == "__main__":
    main()