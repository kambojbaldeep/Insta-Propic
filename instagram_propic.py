from colored import stylize, fg
import instaloader

# Decoration
print(stylize("\n---- | Download Instagram profile picture | ----\n", fg("red")))

# Class
class Downloader:
    def __init__(self, username):
        self.username = username

    # Output magic method
    def __repr__(self):
        try:
            self.download_profilepic(self.username)
            return stylize(f"\nProfile picture of \"{self.username}\" downloaded successfully.\n", fg("green"))
        except instaloader.exceptions.ProfileNotExistsException:
            return stylize(f"\nUser \"{self.username}\" does not exist.\n", fg("red"))

    # Method to download profile picture
    def download_profilepic(self, user):
        session = instaloader.Instaloader()
        session.download_profile(user, profile_pic_only=True)

# Main execution
if __name__ == "__main__":
    # User interaction
    username = input("Enter username: ")

    print(Downloader(username))
