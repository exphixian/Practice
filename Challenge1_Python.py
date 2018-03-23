from datetime import datetime
time = datetime.now()
year = int(time.year)

name = input("What is your name?")
age = int(input("How old are you?"))
old = str(100 - age + year)
message = "You will turn 100 in %s.\n" % (old)

print("Hi %s." % (name))
print(message)

consent = input("Do you want to hear that again?")
if consent == "yes":
    number = int(input("How many times?"))
    print(message * number)
    print("Enjoy your last", 100-age, "years!")
else:
    print("Enjoy your last", 100-age, "years!")
