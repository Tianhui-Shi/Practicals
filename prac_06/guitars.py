from guitar import Guitar

def main():
    guitars_list = []
    print("My guitars!")
    name = input("Name: ")
    while len(name) != 0:
        year = int(input("Year: "))
        cost = float(input("$"))
        new_guitar = Guitar(name,year,cost)
        guitars_list.append(new_guitar)

        print(new_guitar, "added. ")
        name = input("Name: ")

    # add two guitars
    guitars_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))


    print("These are my guitars: ")
    for i, guitar in enumerate(guitars_list):

        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        print("Guitar {0}: {1.name:>24} ({1.year}), worth ${1.cost:15,.2f}{2}".format(i+1, guitar, vintage_string))


if __name__ == '__main__':
    main()