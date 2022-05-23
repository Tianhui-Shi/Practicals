from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi

def main():
    # store the taxi in list as reqiured
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),SilverServiceTaxi("Hummer", 200, 4)]

    # display menu
    menu = "Let's drive!\n q)uit, c)hoose taxi, d)rive"
    print(menu)

    current_taxi = None
    bill = 0

    # start the meun
    user_input = str(input(">>> ")).lower()
    while user_input != 'q':
        if user_input == 'c':
            print("Taxis available: ")
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i,taxi))

            user_taxi = int(input("Choose taxi: "))

            # if current_taxi = taxis[user_taxi] runs, it means input is 0,1,2
            # else it means input is out-range or not number
            try:
                current_taxi = taxis[user_taxi]
            except:
                print("Invalid taxi choice.")

        elif user_input == 'd':
            if current_taxi:
                current_taxi.start_fare()
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name,cost))
                bill += cost
            else:
                print("You need to choose a taxi before you can drive.")
        else:
            print("Invalid taxi choice")

        # print the result and repeat the loop
        print("Bill to date: ${:.2f}".format(bill))
        print(menu)
        user_input = str(input(">>> ")).lower()

main()