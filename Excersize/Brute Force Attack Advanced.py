# Define the correct password
correct_password = "12345"

# Use a while loop to keep asking for the password until the correct one is entered
while True:
    # Prompt the user to enter the password
    user_input = input("Please enter the password: ")
    
    # Check if the entered password is correct
    if user_input == correct_password:
        print("Password accepted! Access granted.")
        break  # Exit the loop if the password is correct
    else:
        print("Incorrect password. Please try again.")

















