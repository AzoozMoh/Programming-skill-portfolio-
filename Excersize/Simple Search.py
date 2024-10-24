# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Prompt the user to enter a search term
p = input("Enter a name to search for: ")

# Search for the term in the list
if p in names:
    print(f"{p} found in the list!")
else:
    print(f"{p} not found in the list.")
