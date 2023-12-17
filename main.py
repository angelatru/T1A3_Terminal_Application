from perfume_functions import add_perfume, remove_perfume, edit_perfume, view_perfume, rec_perfume

file_name = "your_perfume_list.csv"
file_recommend = "perfume_rec_list.csv"

try:
    # open the file in read mode
    todo_file = open(file_name, "r")
    todo_file.close()
    # if it throws error, it means the file doesn't exist
    # if no error, it means the file exist
except FileNotFoundError:
    # Now, we know the file doesn't exist
    # Create the file
    todo_file = open(file_name, "w")
    # We can also insert the first line into the file
    todo_file.write("Name,Company,Gender,TopNotes,MiddleNotes,BaseNotes\n")
    todo_file.close()

print("Welcome to you perfume tracker! Visit Fragrantica at https://www.fragrantica.com/ to find out your perfume's notes")

def menu():
    print("1. Enter 1 to add a perfume to your list")
    print("2. Enter 2 to remove a perfume from your list")
    print("3. Enter 3 to modify perfume details")
    print("4. Enter 4 to view your owned perfumes")
    print("5. Enter 5 to get perfume recommendations")
    print("6. Enter 6 to exit")
    choice = input("Enter your selection: ")
    return choice

users_choice = ""

while users_choice != "6":
    users_choice = menu()
    if (users_choice == "1"):
        add_perfume(file_name)
    elif (users_choice == "2"):
        remove_perfume(file_name)
    elif (users_choice == "3"):
        edit_perfume(file_name)
    elif (users_choice == "4"):
        view_perfume(file_name)
    elif (users_choice == "5"):
        #recommend perfume from existing list
        rec_perfume(file_recommend)
    elif (users_choice == "6"):
        continue
    else:
        print("Invalid Input")

print("Thank you for using this perfume tracker!")
