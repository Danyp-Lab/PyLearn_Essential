# instagram unfollow finder
# be Aware , this lib is not safe . your account is risk , just use in a dummy account
# insta lib , Get pass From User Without Showing
import getpass

import instaloader

old_followers = []
new_followers = []

# add oldFollowers to list
f = open("followers.txt")

for line in f:
    old_followers.append(line)
f.close()

# connect Insta
InstagramInstant = instaloader.Instaloader()

username = input("your username: ")
password = getpass.getpass("your password: ")

InstagramInstant.login(username, password)
print("you have connected successfully")

profile = instaloader.Profile.from_username(InstagramInstant.context, "danielPM307")

for follower in profile.get_followers():
    new_followers.append(follower)

# compare followers
for n_follower in new_followers:
    if n_follower not in old_followers:
        print(n_follower)
f.close()

f = open("followers.txt", "w")
for follower in new_followers:
    f.write(follower + "\n")
f.close()
