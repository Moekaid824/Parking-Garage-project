------------Anifa------------#
class Garage:
    def __init__(self):
        self.tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parking_spaces = ['A','B','C','D','E','F','G','H','I','J']
        self.current_parked_cars = {}
    def park(self):
        welcome = input("Welcome to the parking garage, would you like to enter, leave, or pay? ")
        if welcome.lower() == "enter":
            takes_ticket = input("Would you like to take a ticket (yes or no)? ")
            if takes_ticket.lower() == "yes":
                num_on_parking_ticket = int(input("What is the number on the parking ticket? "))
                your_name = input("What is your name? ")
                if num_on_parking_ticket in self.tickets:
                    self.tickets.remove(num_on_parking_ticket)
                    self.current_parked_cars[your_name] = self.parking_spaces[0]
                    self.parking_spaces.pop(0)
                    print(f"Remaining tickets: {self.tickets} \nParked Cars: {self.current_parked_cars}")
                else:
                    print("Invalid ticket number.")
            else:
                print("Alright, you cannot park here.\nHave a nice day!")
        elif welcome.lower() == "leave":
            self.leave_garage()
        elif welcome.lower() == "pay":
            self.pay_for_parking()

 #------------------Moe-----------------#
    def pay_for_parking(self):
        ticket_cost = 15
        pay_ticket = input("Are you ready to leave the parking lot (yes or no)? ")
        if pay_ticket.lower() == "yes":
            hours = int(input("How many hours have you been here? "))
            total = ticket_cost * hours
            print(f"This is the cost of your ticket: {total}")
            how_to_pay_ticket = input("What payment method would you like to use (card or mobile pay)? ")
            if how_to_pay_ticket.lower() == "card" or how_to_pay_ticket.lower() == "mobile pay":
                amount = int(input("Input the amount that you want to pay: $"))
                if total == amount:
                    print("Your ticket has been paid. You have 15 minutes to leave, Have a good day!")
                else:
                    print("Invalid payment amount.")
            else:
                print("We do not accept that payment method. Please choose a correct payment method.")
        else:
            print("Enjoy your time here.")

    def leave_garage(self):
        car_leave = input("Are you ready to leave the parking lot (yes or no)? ")
        if car_leave.lower() == "yes":
            self.tickets.append(1)
            self.parking_spaces.append(1)
            name = input("What is the name of the owner of the ticket: ")
            if name in self.current_parked_cars:
                del self.current_parked_cars[name]
            print(f"{name}'s car has been removed from the parking lot.")
        else:
            print("This person does not have a car parked in the lot.")

garage=Garage()
garage.park()
