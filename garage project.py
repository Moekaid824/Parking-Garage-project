# ------------Anifa------------#
class Garage:
    def __init__(self):
        self.tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parking_spaces = ['A','B','C','D','E','F','G','H','I','J']
        self.current_parked_cars = {}
        self.ready_to_leave = {}

    #Runner Method 
    def myrunner(self):
        #Loop through different action of garage (park,pay,leave) 
        while True:
            welcome = input("Welcome to the parking garage, would you like to enter, leave, or pay?: ")
            if welcome.lower() == "enter":
                self.park()
            elif welcome.lower() == "leave":
                self.leave_garage()
            elif welcome.lower() == "pay":
                self.pay_for_parking()
            else:
                print("Invalid input, try again.")

    def park(self):
        takes_ticket = input("Would you like to take a ticket (yes or no)?: ")
        if takes_ticket.lower() == "yes" or takes_ticket.lower() == "y":
            if len(self.tickets) < 1: #If there is no tickets left, you cannot receive a ticket
                print("Sorry, no more spots available.")
                return
            ticket = self.tickets.pop(0) #Take a ticket fromt he list
            parking_spot = self.parking_spaces.pop(0) #Take parking spot from list
            self.current_parked_cars[ticket] = parking_spot #Assign a parking spot to a ticket
            print(f"Your parking ticket is {ticket} and your parking spot is {parking_spot}.")
            print(f"Remaining tickets: {self.tickets} \nParked Cars: {self.current_parked_cars}")

 #------------------Moe-----------------#
    def pay_for_parking(self):
        ticket_cost = 15
        pay_ticket = input("Are you ready to pay (yes or no)?: ")
        if pay_ticket.lower() == "yes" or pay_ticket.lower() == "y":
            ticket_num = int(input("What is your ticket number?: "))
            if ticket_num not in self.current_parked_cars: #If the ticket wasn't assigned to a car, you cannot pay for it
                print("Sorry, there is no ticket with that ticket number.")
                return
            hours = int(input("How many hours have you been here?: "))
            total = ticket_cost * hours
            print(f"This is the cost of your ticket: ${total}")
            pay = input("Are you ready to pay?(Y/N): ") 
            if pay.lower() == "yes" or pay.lower() == "y":
                self.ready_to_leave[ticket_num] = self.current_parked_cars[ticket_num] #If the tikect is payed, add ticket num and parking spot to dict of cars that can leave
                print("You have successfully paid your ticket!")
            else:
                print("Ok")
                return    
        else:
            print("Enjoy your time here.")

    def leave_garage(self):
        car_leave = input("Are you ready to leave the parking lot (yes or no)?: ")
        if car_leave.lower() == "yes":
            ticket_num = int(input("What is your ticket number?: "))
            if ticket_num not in self.current_parked_cars: #If ticket number is not assigned, it is not a valid ticket
                print("Sorry, there is no ticket with that ticket number.")
                return
            elif ticket_num not in self.ready_to_leave: #If your ticket number is assigned, but wasn't payed for, you cannot leave
                print("Sorry, you still have to pay for your ticket.")
                return
            else: #Ready to leave
                self.tickets.append(ticket_num) #Add ticket back into available ticket list
                self.parking_spaces.append(self.current_parked_cars[ticket_num]) #Add parking spot back into available parking spot list 
                #Remove ticket num and asssigned parking spot now that ticket has been added back into available list
                del self.current_parked_cars[ticket_num] 
                del self.ready_to_leave[ticket_num]    
                print("Thank you for parking with us, have a nice day!")
        else:
            print("Fine, have a nice day!")

    
garage=Garage()
garage.myrunner()
