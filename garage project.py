


























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
