## Prgram that takes integers from user until 0 is entered, stores them in a
# list, sorts them into descending order and displays the sorted list. ###

list = []
entry = int(input("Please enter an integer to add to list (0 to exit): "))

while entry != 0:
    list.append(entry)
    entry = int(input("Please enter an integer to add to list (0 to exit): "))

list.sort(reverse=True)
print(list)
