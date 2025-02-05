from guitar import Guitar
def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    # add two guitar
    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.9)

    # print the result
    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 95,guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other.name, 5,other.get_age()))
    print()
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name,True,guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other.name,False,other.is_vintage()))


if __name__ == '__main__':
    main()