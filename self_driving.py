def move_forward():
    print("moving forward")


def turn(direction):
    print(f"turning {direction}")


def start_engine():
    print("starting engine")


def stop_engine():
    print("stopping engine")


destination = input("Where do you want to go? ")

start_engine()
move_forward()

if destination == "school":
    turn("right")
    print("We arrived at school!")
elif destination == "grocery store" or destination == "dentist":
    turn("left")
    move_forward()
    if destination == "grocery store":
        turn("left")
        print("We arrived at grocery store!")
    else:
        turn("right")
        print("We arrived at dentist!")
elif destination == "restaurant":
    turn("go straight")
    print("We arrived at restaurant!")
else:
    print("Invalid destination")
