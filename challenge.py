# pin = "pin"

# # TODO: Ask the user to enter a pin and guess the correct pin
# guessed_password = input("Enter your pin: ")


# if guessed_password == pin:
#     print("Success! You guessed the correct pin.")
# else:
#     print("Incorrect pin. Please try again.")
#     guessed_password = input("Enter your pin: ")
#     if guessed_password == pin:
#         print("Success! You guessed the correct pin.")
#     else:
#         print("Incorrect pin. You have reached the maximum number of incorrect guesses.")
#         play_again = input("Do you want to play again? (yes/no): ")
#         if play_again.lower() == "yes":
#             guessed_password = input("Enter your pin: ")
#             if guessed_password == pin:
#                 print("Success! You guessed the correct pin.")
#             else:
#                 print("Incorrect pin. You have reached the maximum number of incorrect guesses.")
#         else:
#             print("Thank you for playing!")


pin = "pin"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    guessed_password = input("Enter your pin: ")
    
    if guessed_password == pin:
        print("Success! You guessed the correct pin.")
        break
    else:
        attempts += 1
        print("Incorrect pin. Please try again.")
        if attempts == max_attempts:
            print("You have reached the maximum number of incorrect guesses.")
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() == "yes":
                attempts = 0  
            else:
                print("Thank you for playing!")
