from capybara import Capybara

capybara1 = Capybara("Larz", "M", 5)
capybara2 = Capybara("Glennzel", "M", 3)
capybara3 = Capybara("Ralph", "M", 7)

capybaras = [capybara1, capybara2, capybara3]

test_case = int(input("Enter the test case number: "))

if 1 <= test_case <= len(capybaras):
    selected_capybara = capybaras[test_case - 1]
    print(f"Test Case {test_case}: Name: {selected_capybara.name}, Gender: {selected_capybara.gender}, Age: {selected_capybara.age} years old")
else:
    print("Invalid test case number.")

