from pathlib import Path

path = Path("guest.txt")

i = 0
user_names = ""

while i < 3:
    user_name = input("Please enter your name: ")
    user_names += (user_name + "\n")
    i += 1

path.write_text(user_names)

