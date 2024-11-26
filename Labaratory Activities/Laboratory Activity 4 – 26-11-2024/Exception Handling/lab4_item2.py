try:
    # Ask the user to input the size of the array
    size = int(input("Enter the size of the array: "))
    
    # Initialize the array with zeros
    arr = [0.0] * size

    # Prompt the user to input the elements of the array
    print("Enter the elements of the array:")
    for i in range(size):
        arr[i] = float(input())

    # Ask the user for the index to print
    x = int(input("Enter the index of the element to print: "))

    # Print the element at index x with 2 decimal places
    print(f"Element at index {x}: {arr[x]:.2f}")

# Handle invalid index errors
except IndexError:
    print(f"Index {x} is invalid.")

# Handle other unexpected errors
except ValueError:
    print("Invalid input. Please enter numbers only.")