def move_forward():
    print("moving forward")


def turn(direction):
    print(f"turning {direction}")


def start_engine():
    print("starting engine")


def stop_engine():
    print("stopping engine")


def follow_roundabout(exit_number):
    print(f"taking exit number {exit_number} from the roundabout")


start_engine()

destination = input("Where do you want to go? ")


if destination == "library":
    move_forward()
    turn("left")
    print("We arrived at library!")
elif destination == "tech park":
    move_forward()
    turn("right")
    print("We arrived at tech park!")
elif destination in ["hospital", "mall", "airport", "university", "stadium"]:
    move_forward()
    print("Entering the roundabout")

    if destination == "hospital":
        follow_roundabout("1st exit")
        print("We arrived at hospital!")
    elif destination == "mall":
        follow_roundabout("2nd exit")
        move_forward()
        turn("right")
        print("We arrived at mall!")
    elif destination == "airport":
        follow_roundabout("3rd exit")
        print("We arrived at airport!")
    elif destination in ["university", "stadium"]:
        follow_roundabout("4th exit")
        move_forward()
        if destination == "university":
            turn("left")
            print("We arrived at university!")
        elif destination == "stadium":
            turn("right")
            print("We arrived at stadium!")

else:
    print("Oh no! Destination not recognized.")

stop_engine()
