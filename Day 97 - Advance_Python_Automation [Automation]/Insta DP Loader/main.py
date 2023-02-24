from instaloader import Instaloader

username = input("Enter IG username: ")

loader = Instaloader()
loader.download_profile(username, profile_pic_only=True)  # download profile pictures