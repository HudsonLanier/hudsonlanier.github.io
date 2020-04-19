TICKET_PRICE = 10

tickets_remaining = 100  

SERVICE_FEE = 5

def calculate_price(number_of_tickets):
    return number_of_tickets * TICKET_PRICE + SERVICE_FEE

while tickets_remaining > 0:
    print("There are {} tickets remaining.".format(tickets_remaining))
    username = input("What is your name?  ")
    try:
        tickets_desired = int(input("Hello {}, how many tickets would you like?".format(username)))
        if tickets_remaining - tickets_desired <= 0:
            raise ValueError("there are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
            print("Oh no, we ran into an issue. {} Please try again".format(err))
    else:        
        order_cost = calculate_price(tickets_desired)
        print("The cost of your tickets is ${}.".format(order_cost))
        order_confirmation = input("would you like to proceed with the purchase? Hit 'Y' for Yes or 'N' for no.  ").upper()
        if order_confirmation == "Y":
            print("SOLD!")
            tickets_remaining -= tickets_desired
        else:
            print("Thanks for visiting the store {}.".format(username))
print("The tickets are sold out.")
    
    
