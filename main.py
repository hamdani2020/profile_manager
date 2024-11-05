import os

current_user_directory = __import__("profile").current_user_directory
get_profile = __import__("profile").get_profile
read_profile = __import__("profile").read_profile
update_profile = __import__("profile").update_profile


def main():
    current_directory, username = current_user_directory()
    current_dir = os.getcwd()

    # Checks if the current working directory matches the user's username directory
    if os.path.basename(current_dir) == username:
        profile_path = get_profile(current_dir)

        # Check if the profile.txt file exists
        if os.path.isfile(profile_path):
            read_profile(profile_path)

            confirm = (
                input("This is your updated information? (yes/no): ").strip().lower()
            )
            if confirm != "yes":
                update_profile(profile_path)
            else:
                print("Profile information is up to date")
        else:
            print("Profile file not found. Create a new profile")
            update_profile(profile_path)

    else:
        user_directory = os.path.join(current_directory, username)
        os.makedirs(user_directory, exist_ok=True)
        profile_path = get_profile(user_directory)

        print(f"New directory created at {user_directory}.")
        update_profile(profile_path)


if __name__ == "__main__":
    main()
