def check_even_odd(number):
    """Determine if the number is even or odd and return a message."""
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    # Ask the user for a number
    user_input = int(input("Enter a number: "))
    
    # Pass the entered number to the function and get the result
    result = check_even_odd(user_input)
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()
















