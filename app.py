import functions


while True:
    print("=====================================")  
    print("Welcome to the Train Booking System v0.0.1")
    print("1. Check available seats")
    print("2. Book a seat")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        functions.get_available_seats()
    elif choice == '2':
       functions.book_seat()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")