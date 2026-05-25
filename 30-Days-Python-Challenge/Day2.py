# Write a function called convert_add that takes a list of strings as an 
# argument and converts it to integers and sums the list. For example 
# [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and summed to 9.

# Read in the string list
# Use list comprehension to convert the strings to integers
# Then Sum the elements


def convert_add(string_list):
    integer_list = [int(i) for i in string_list] # TypeCasting the strings to integers

    sum = 0
    for i in integer_list:
        sum += i
    return sum

count = 0
length = int(input("How many elements do you wish to input: "))

# Test 
# string_list = ['1','3','5']
# print(convert_add(string_list))

string_list = []

while True:
    
    if count == length: # Condition for the termination of the while loop

        # ValueError handling, so that the program will not terminate with an error if another datatype is inputed 
        try:
            sum = convert_add(string_list)
        except ValueError:
            print("Input Numbers Only!")
            count = 0
            string_list.clear()
            continue
        print(f"The sum of the list elemnts is: {sum}") 
        break

    # Getting input fom the user and reading it into the list.
    element = input(f"Element {count + 1}: ")
    string_list.append(element) 

    count += 1