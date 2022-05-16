from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    menu = "Let's drive!\n q)uit, c)hoose taxi, d)rive"
    print(menu)
    user_input = str(input(">>> ")).lower()
    while user_input != 'q':
        if user_input not in ["q", "c", "d"]:
            print("Invalid option")


main()