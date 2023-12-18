import csv
import random

# Sets of popular gendered notes
feminine_popular = {'Bergamot','Lavender','Vanilla','Amber','Musk','Patchouli','Rose','Musk','Neroli','Ylang-Ylang','Jasmine'}
masculine_popular = {'Lavender','Sage','Rosemary','Anise','Cedarwood','Tabacco','Cinnamon','Leather','Mint','Nutmeg','Bergamot'}
unisex_popular = {'Lavender','Mandarin','Sandalwood','Papyrus','Basil','Ginger','Patchouli','Rosemary','Violet','Heliotrope'}

gender_list = ['feminine', 'masculine', 'unisex']
perfume_categories = ['Name', 'Company', 'Gender', 'TopNotes', 'MiddleNotes', 'BaseNotes']

def view_perfume_option(file_name):
    view_option = input("Would you like to view your perfumes? Enter 'y', otherwise enter to continue: ")
    if view_option == 'y':
        view_perfume(file_name)

# Add function
def add_perfume(file_name):
    print("Add a perfume! Visit Fragrantica at https://www.fragrantica.com/ to see your perfume details.")
    perfume_name = input("Enter the name of the perfume: ")
    perfume_company = input("Enter the brand/comapny/creator of the perfume: ")
    perfume_gender = input("Enter the gender of the perfume (feminine, masculine, unisex): ")
    perfume_topnotes = input("Enter the TOP notes seperated by a '/' (eg. vanilla/burbon): ")
    perfume_middlenotes = input("Enter the MIDDLE notes seperated by a '/' (eg. vanilla/burbon): ")
    perfume_basenotes = input("Enter the BASE notes seperated by a '/' (eg. vanilla/burbon): ")
    # Open file - list.csv
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        # Insert values of name, brand, gender, and tiered notes
        writer.writerow([perfume_name, perfume_company, perfume_gender, perfume_topnotes, perfume_middlenotes, perfume_basenotes])

    print(f"'{perfume_name}' by {perfume_company} was added to your perfume collection.")

# Remove function
def remove_perfume(file_name):
    # Ask if user wants to view list to get the name of perfume to be removed
    view_perfume_option(file_name)

    perfume_name = input("Enter the name of the perfume that you want to remove: ")

    new_perfume_list = []

    # Track perfume to see if user input is found in collection
    perfume_found = False

    # Remove perfume if user input is the same as the name of the perfume in the list
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if perfume_name != row[0]:
                new_perfume_list.append(row)
            else:
                perfume_found = True
    
    # Code block if perfume is already removed from the collection (not found) or does exist and has been removed.
    if not perfume_found:
        print(f"There is no '{perfume_name}' in your collection.")
    else:
        print(f"The perfume '{perfume_name}' was removed.")

    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(new_perfume_list)
    
    


# Modify function
def edit_perfume(file_name):
    view_perfume_option(file_name)

    # Empy list for new information
    updated_rows = []

    # Enter the name of the perfume user wants to edit and which of the details within the perfume user wants to edit
    edit_perfume_name = input("Enter the name of the perfume which details you want to change?: ")
    edit_perfume_target = input("Which section did you want to edit? (Name, Company, Gender, TopNotes, MiddleNotes, or BaseNotes)?: ")

    try:
        # Finding index value of input target
        index_value = perfume_categories.index(edit_perfume_target)
    except ValueError:
        print("Invalid category entered. Please enter exactly the options provided.")
        return edit_perfume(file_name)
    
    
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
                perfume_found = True
                 
            # Append new information 
            updated_rows.append(row)

    # While iterating over the CSV, is the perfume is not found, prints statement
    if not perfume_found:
        print(f"Perfume not found in your collection. Please ensure the spelling is correct!")
    else:
        print(f"The {edit_perfume_target} for '{edit_perfume_name}' has been successfully changed.")
    
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

         
def rec_perfume(file_recommend):
    # Enter qualities of perfume user would like
        # gender, topnotes, middlenotes, basenotes
    recommendations = []

    while True:
        gender_preferences = input("What gender would you like your perfume to lean towards (feminine, masculine, or unisex)?: ").lower()
        if gender_preferences in gender_list:
            break  # Break the loop if the input is one of the selections
        print("Please enter one of the three options.")

    # Displays different notes popular notes depending on the user input
    if gender_preferences == gender_list[0]:
        print(f"Here are some popular feminine notes if you need some help!: {', '.join(feminine_popular)}")
    elif gender_preferences == gender_list[1]:
        print(f"Here are some popular masculine notes if you need some help!: {', '.join(masculine_popular)}")
    elif gender_preferences == gender_list[2]:
        print(f"Here are some popular unisex notes if you need some help!: {', '.join(unisex_popular)}")

    # Create a list of user notes preferences
    notes_preferences = input("What notes would you like your perfume to have (please seperate by '/')?: ")
    notes_preferences = notes_preferences.lower().split('/')
    
    # Whether the user wants to find perfume notes inclusive or exclusive
    inclusive_option = input("Type 'all' if you want ALL NOTES specified to be included in your perfume recommendations, otherwise enter for ANY of the notes provided: ").lower()

    # Due to weird latin letters, requires encoding change for this function to read the rec list CSV in particular
    with open(file_recommend, "r", encoding='ISO-8859-1') as f:
        reader = csv.reader(f)
        for row in reader:
            # Get the gender of each perfume
            perfume_gender = row[2].lower()
            # Combine all scent notes and split 
            perfume_attributes = row[3].lower() + '/' + row[4].lower() + '/' + row[5].lower()
            perfume_attributes = perfume_attributes.split('/')

            # Check for exclusive AND (all of the specified notes)
            if inclusive_option == 'all':
                if all(note in perfume_attributes for note in notes_preferences) and perfume_gender == gender_preferences:
                    perfume_info = (row[0], row[1], row[3], row[4], row[5])
                    recommendations.append(perfume_info)

            # Default is inclusive OR (any of the specified notes)
            else:
                if any(note in perfume_attributes for note in notes_preferences) and perfume_gender == gender_preferences:
                    perfume_info = (row[0], row[1], row[3], row[4], row[5])
                    recommendations.append(perfume_info)
            
    
    # If there are recommendations found in the list
    if recommendations:
        # Generates how many outputs the user would like
        num_input = input("How many recommendations would you like?: ")
        print("Here are some perfumes based on your preferences:")
        # Count is used to number the outputs - readability
        count = 1
        # Getting random recommendations, make it more fun  :)
        num_recommendations = min(int(num_input), len(recommendations))
        random_recommendations = random.sample(recommendations, num_recommendations)
        for perfume in random_recommendations:
            print(f" {count}. {perfume[0]} by {perfume[1]}")
            print(f"Top Notes: {perfume[2]}")
            print(f"Middle Notes: {perfume[3]}")
            print(f"Base Notes: {perfume[4]}")
            print("------------------------------")

            count += 1
    else:
        print("Sorry, there are no recommendations that suit your preferences.")
    

