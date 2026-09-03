# PR. 2 - Logic Box
# Pattern Generator and Number Analyzer
print("=" * 50)
print(" Welcome to the Pattern Generator and Number Analyzer!")
print("=" * 50)

print("\nThis program allows you to:")
print("1. Generate a right-angled triangle pattern")
print("2. Analyze a range of numbers")
print("3. Exit the program")


# Main program loop
while True:

    print("\n" + "-" * 40)
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")
    # OPTION 1: PATTERN GENERATION
    if choice == "1":

        while True:
            try:
                rows = int(input("Enter the number of rows for the pattern: "))

                # Check whether rows are positive
                if rows <= 0:
                    print("Error: Number of rows must be positive.")

                    # Demonstrating break
                    print("Pattern generation stopped.")
                    break

                print("\nPattern:")

                # Nested loops for pattern generation
                for i in range(1, rows + 1):

                    for j in range(1, i + 1):
                        print("*", end="")

                    print()

                break

            except ValueError:
                print("Error: Please enter a valid integer.")

    # OPTION 2: NUMBER ANALYSIS
    elif choice == "2":

        while True:
            try:
                start = int(input("Enter the start of the range: "))
                end = int(input("Enter the end of the range: "))

                # Validate range
                if end < start:
                    print("Error: End of the range must be greater than or equal to start.")
                    continue

                print()

                total = 0

                # Analyze every number in the range
                for number in range(start, end + 1):

                    # Demonstrating pass
                    if number is None:
                        pass

                    # Check whether number is even or odd
                    if number % 2 == 0:
                        print("Number", number, "is Even")
                    else:
                        print("Number", number, "is Odd")

                    # Calculate sum
                    total += number

                print("\nSum of all numbers from", start, "to", end, "is:", total)

                break

            except ValueError:
                print("Error: Please enter valid integer values.")
                continue

    # OPTION 3: EXIT
    elif choice == "3":

        print("\nExiting the program. Goodbye!")
        break

    # INVALID MENU OPTION
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
        continue