import time
import os.path
if not os.path.isfile("./settings.txt"):
    open("settings.txt", "w")
settings_file = open("settings.txt", "r+")
settings = settings_file.read()
mining_yield = 0
def get_yield():
    return input("Enter your yield (use decimal points instead of comma!): ")
def update_settings():
    mining_yield = get_yield()
    settings_file.write(mining_yield)
    return mining_yield
if not settings or settings == "":
    mining_yield = update_settings()
else:
    mining_yield = float(settings)

asteroid_size = input("Enter asteroid size, or \"x\" if you'd like to change your yield: ")
if(asteroid_size == "x"):
    mining_yield = update_settings()
    asteroid_size = input("Enter asteroid size:")
timer = int(asteroid_size) / float(mining_yield)
print("Setting timer for {0}".format("{0} seconds".format(timer) if timer < 60 else "{0} minutes".format(timer / 60)))
while(timer > 0):
    if timer > 60:
        print("{0} minutes left!".format(timer / 60))
        time.sleep(60)
        timer = timer - 60
    elif timer > 10:
        print("{0} seconds left!".format(timer))
        time.sleep(5)
        timer = timer - 5
    else:
        print("{0} seconds left!".format(timer))
        time.sleep(1)
        timer = timer - 1
print("Mining process complete, press \"ctrl+c\" to terminate\a")
while(True):
    print("\a")
    time.sleep(5)