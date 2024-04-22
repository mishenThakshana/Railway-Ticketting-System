import data

def get_available_seats():
    print("=====================================")  
    print("Available seats:")
    for seat in data.booked_seats:
        print(seat["train_class"] + " " + str(seat["total_seats"] - seat["booked_seats"]))
    return

def book_seat():
    print("=====================================")  
    print("Booking a seat")
    print("Destinations: A/B/C")
    starting_destination = input("Enter your starting destination: ").upper()
    if starting_destination not in ['A', 'B', 'C']:
        print("Invalid destination.")
        choice = input("Do you want to try again? (y/n): ")
        if choice == 'y':
            book_seat()
        else:
            return
    else: 
        available_ending_destinations = []
        for dest in ['A', 'B', 'C']:
            if dest != starting_destination:
                available_ending_destinations.append(dest)
        print("Available ending destinations: " + "/".join(available_ending_destinations))        
        ending_destination = input("Enter your ending destination: ").upper()
        if ending_destination not in available_ending_destinations:
            print("Invalid destination.")
            choice = input("Do you want to try again? (y/n): ")
            if choice == 'y':
                book_seat()
            else:
                return
        else:
            print("Available classes: First Class (1)/Business Class (2)/Economy Class (3)")
            train_class = input("Enter your preferred class: ")
            if train_class not in ['1', '2', '3']:
                print("Invalid class.")
                choice = input("Do you want to try again? (y/n): ")
                if choice == 'y':
                    book_seat()
                else:
                    return
            else:
                train_class = int(train_class)
                if data.booked_seats[train_class - 1]["booked_seats"] < data.booked_seats[train_class - 1]["total_seats"]:
                    no_of_seats = int(input("Enter the number of seats you want to book: "))
                    if no_of_seats <= data.booked_seats[train_class - 1]["total_seats"] - data.booked_seats[train_class - 1]["booked_seats"]:
                        data.booked_seats[train_class - 1]["booked_seats"] += no_of_seats
                        print("Seat(s) booked successfully.")
                    else:
                        print("No available seats in the selected class.")
                        choice = input("Do you want to try again? (y/n): ")
                        if choice == 'y':
                            book_seat()
                        else:
                            return
                else:
                    print("No available seats in the selected class.")
                    choice = input("Do you want to try again? (y/n): ")
                    if choice == 'y':
                        book_seat()
                    else:
                        return
    return