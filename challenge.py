# password = "password"

# # TODO: Ask the user to enter a password and guess the correct password
# guessed_password = input("Enter your password: ")


# if guessed_password == password:
#     print("Success! You guessed the correct password.")
# else:
#     print("Incorrect password. Please try again.")
#     guessed_password = input("Enter your password: ")
#     if guessed_password == password:
#         print("Success! You guessed the correct password.")
#     else:
#         print("Incorrect password. You have reached the maximum number of incorrect guesses.")
#         play_again = input("Do you want to play again? (yes/no): ")
#         if play_again.lower() == "yes":
#             guessed_password = input("Enter your password: ")
#             if guessed_password == password:
#                 print("Success! You guessed the correct password.")
#             else:
#                 print("Incorrect password. You have reached the maximum number of incorrect guesses.")
#         else:
#             print("Thank you for playing!")


password = "password"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    guessed_password = input("Enter your password: ")
    
    if guessed_password == password:
        print("Success! You guessed the correct password.")
        break
    else:
        attempts += 1
        print("Incorrect password. Please try again.")
        if attempts == max_attempts:
            print("You have reached the maximum number of incorrect guesses.")
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() == "yes":
                attempts = 0  
            else:
                print("Thank you for playing!")
