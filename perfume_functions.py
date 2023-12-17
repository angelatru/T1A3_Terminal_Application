import csv

# Add function
def add_perfume(file_name):
    print("Add a perfume! Visit Fragrantica at https://www.fragrantica.com/ to see you perfume details.")
    perfume_name = input("Enter the name of the perfume: ")
    perfume_company = input("Enter the brand of the perfume: ")
    perfume_gender = input("Enter the gender of the perfume (feminine, masculine, unisex): ")
    perfume_topnotes = input("Enter the TOP notes seperated by a '/' (eg. vanilla/burbon): ")
    perfume_middlenotes = input("Enter the MIDDLE notes seperated by a '/' (eg. vanilla/burbon): ")
    perfume_basenotes = input("Enter the BASE notes seperated by a '/' (eg. vanilla/burbon): ")
    # Open file - list.csv
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        # Insert values of name, brand, gender, and tiered notes
        writer.writerow([perfume_name, perfume_company, perfume_gender, perfume_topnotes, perfume_middlenotes, perfume_basenotes])

    print(f"{perfume_name} by {perfume_company} was added to your perfume collection.")

# Remove function
def remove_perfume(file_name):
    perfume_name = input("Enter the name of the perfume that you want to remove: ")
    new_perfume_list = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (perfume_name != row[0]):
                new_perfume_list.append(row)
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(new_perfume_list)
    
    print(f"{perfume_name} was removed.")


# Modify function
def edit_perfume(file_name):
    # Empy list for new information
    updated_rows = []
    # Enter the name of the perfume user wants to edit and which of the details within the perfume user wants to edit
    edit_perfume_name = input("Enter the name of the perfume which details you want to change?: ")
    edit_perfume_target = input("Which section did you want to edit? (Name, Company, Gender, TopNotes, MiddleNotes, or BaseNotes)?: ")
    # Perfume categories
    perfume_categories = ['Name', 'Company', 'Gender', 'TopNotes', 'MiddleNotes', 'BaseNotes']
    
    try:
        # Finding index value of input target
        index_value = perfume_categories.index(edit_perfume_target)
    except ValueError:
        print("Invalid category entered. Please try selection 3 again.")
        return
    
    # This is to track is the perfume is in the list of collection
    perfume_found = False

    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == edit_perfume_name:
                print(f"Current details: {row[index_value]}")
                new_value = input(f"Enter new {edit_perfume_target}: ")

                # Update the specific field based on user input
                row[index_value] = new_value
            
            # Append new information 
            updated_rows.append(row)

    # While iterating over the CSV, is the perfume is not found, prints statement
    if not perfume_found:
        print(f"The perfume '{edit_perfume_name}' is not found in your collection. Please ensure the spelling is correct!")
        return
    
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(updated_rows)
                



# View function
def view_perfume(file_name):
    print("Here is your list of perfumes")
    print("------------------------------")
    # Number the list of perfumes
    count = 1
    # Open CSV and show details of each row
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            print(f"{count}.")
            print(f"{row[0]} by {row[1]} ({row[2]})")
            print(f"Top Notes: {row[3]}")
            print(f"Middle Notes: {row[4]}")
            print(f"Base Notes: {row[5]}")
            print("------------------------------")

            count += 1


# Recommendation function
def rec_perfume():
    pass
