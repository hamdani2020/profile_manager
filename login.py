import os

def current_user_directory():
    """ This function gets the user current working directory"""
    current_directory = os.getcwd()
    username = os.path.basename(current_directory)
    return current_directory, username


def get_profile(user_directory):
    """ This function gets the path to the profile.txt file."""
    return os.path.join(user_directory, ".profile.txt")


def read_profile(profile_path):
    """ Read and display the profile of data if it exists."""
    with open(profile_path, "r") as file:
        content = file.read().strip()
        print("Recent profile data")
        print(content)
    return content


def update_profile(profile_path):
    """Prompt user for new data if not exists"""
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")
    with open(profile_path, 'w') as file:
        file.write(f"Name: {name}\nPhone: {phone_number}\nEmail: {email}")
    print("Profile updated successfully.")    
