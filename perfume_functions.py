import csv

# Add function
def add_perfume(file_name):
    print("Add a perfume")
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

# Remove function
def remove_perfume():
    pass


# Modify function
def edit_perfume():
    pass

# View function
def view_perfume():
    pass

# Recommendation function
def rec_perfume():
    pass