# Program to demonstrate different Python string methods
try:
    # Read string from user
    text = input("Enter a string: ")

    # Convert to uppercase
    print("\nUppercase:", text.upper())

    # Convert to lowercase
    print("Lowercase:", text.lower())

    # Split the string
    delimiter = input("\nEnter a delimiter to split the string: ")
    print("Split Result:", text.split(delimiter))

    # Replace a substring
    old = input("\nEnter the substring to replace: ")
    new = input("Enter the new substring: ")
    print("After Replace:", text.replace(old, new))

    # Find a character or substring
    search = input("\nEnter character or substring to find: ")
    index = text.find(search)

    if index != -1:
        print(search, "found at index", index)
    else:
        print(search, "not found in the string.")

except Exception as e:
    print("Error:", e)
