from guitar import Guitar

def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while len(name) != 0:
        year = int(input("Year: "))
        cost = float(input("$"))
        new_guitar = Guitar(name,year,cost)
        guitars.append(new_guitar)

        print(new_guitar, "added. ")
        name = input("Name: ")





if __name__ == '__main__':
    main()