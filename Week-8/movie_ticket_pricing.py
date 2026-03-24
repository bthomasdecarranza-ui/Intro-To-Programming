while True:
    user_input = input("Enter your age (or type 'quit' to exit): ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    age = int(user_input)

    if age < 12:
        price = 8
    elif age >= 65:
        price = 10
    else:
        price = 15

    print(f"Your ticket price is ${price}.")
    