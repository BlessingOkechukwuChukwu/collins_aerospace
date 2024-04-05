import random
from cryptography.fernet import Fernet

# python task that gets a list of airport terminals, flight pilot (captain), and airplines

# For a flight from terminal A to B, randomly assign a pilot and an aircraft to the customer 

# To do 
# -request customers' name 
# -show avalable terminals with the terminal code beside it
# -request the terminal code from the customer (takeoff terminal). 
# -request the terminal code from the customer (destination terminal).
# - if takeoff and destination terminal code are the same, ask user to input destination code again 
# - encrypt customers name and use it as boarding pass

class Aerospace:
    def __init__(self):
        self.terminals = {
            "uk100": "London Airport",
            "uk101": "Edinburgh Airport",
            "uk102": "Manchester Airport",
            "uk103": "Heathrow Airport"
        }

        self.flight_captains = {
            "pilot1": "Blessing",
            "pilot2": "Vincent",
            "pilot3": "Amy Dean",
            "pilot4": "Nick Ayres",
            "pilot5": "Fatima Ibrahim",
            "pilot6": "Elon Musk"
        }

        self.airlines = {
            "boeing-125": "British Airways",
            "piper-pa-28": "Ethiopian Airlines",
            "cessna-172": "Lufthansa Air"
        }

    def requestCustomerInfo(self):
        self.customer_name = input("Please Enter Your Name: ")
        print("Available Terminals\n")

    def encrypt(self):
        key = Fernet.generate_key()
        fernet = Fernet(key)
        enc_customer_name = fernet.encrypt(self.customer_name.encode())
        self.dcpt_customer_name = fernet.decrypt(enc_customer_name).decode()
        boarding_pass_no = random.randint(100, 999)
        self.boarding_pass = self.dcpt_customer_name + str(boarding_pass_no)

    def requestFlightRoute(self):
        for key in self.terminals:
            print(f"{self.terminals[key]} - Terminal Code is {key}")

        takeoff_terminal = input("Enter Takeoff terminal using the code above: ")
        trial = 1
        while trial > 0:
            destination_terminal = input("Enter destination terminal using the code above: ")

            if destination_terminal == takeoff_terminal:
                print("Takeoff and destination terminal cannot be the same\n")
                trial += 1
            else:
                pilot_id, pilot_name = random.choice(list(self.flight_captains.items()))
                airline_id, airline_name = random.choice(list(self.airlines.items()))
                print(f"Hello {self.customer_name}, your flight from {self.terminals[takeoff_terminal]} to {self.terminals[destination_terminal]} has been scheduled with {airline_name}")
                print(f"Pilot Name: {pilot_name}")
                print(f"Boarding Pass: {self.boarding_pass}")
                break

# create an instance of Aerospace class
main = Aerospace()
main.requestCustomerInfo()
main.encrypt()  # Call encrypt method before requestFlightRoute
main.requestFlightRoute()

