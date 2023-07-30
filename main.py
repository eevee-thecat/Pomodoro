import time

from desktop_notifier import DesktopNotifier

notifier = DesktopNotifier()

def tsec(tmin):
    return tmin * 60

def countdown(t, label):
    while t:
        min = int(t / 60)
        sec = int(t % 60)
        print(f"{label}: {min:02d}:{sec:02d}", end="")
        time.sleep(0.1)
        print("\r", end="")
        t -= 1

def pomodoro (work_time, rest_time, cycles):
    for x in range(cycles):
        countdown(work_time, "Work Timer")
        notifier.send_sync(title="Pomodoro Timer", message="Ding! Break time :)")
        countdown(work_time, "Rest Timer")
        notifier.send_sync(title="Pomodoro Timer", message="Ding! Break time is over, back to work :)")


print("WELCOME TO POMODORO TIMER\n")
cont = True
while cont:
    invalid = True
    while invalid:
        invalid = False
        work_time = input("How long would you like to study for? Enter in minutes. ")
        try:
            work_time = int(work_time)
        except ValueError:
            print("That was not a valid number. Please try again. ")
            invalid = True

        if not invalid and work_time < 1:
            print("Please enter a time greater than 0.")
            invalid = True

    invalid = True
    while invalid:
        invalid = False
        rest_time = input("How long would of a break would you like in between study sessions? Enter in minutes. ")
        try:
            rest_time = int(rest_time)
        except ValueError:
            print("That was not a valid number. Please try again. ")
            invalid = True

        if not invalid and rest_time < 1:
            print("Please enter a time greater than 0.")
            invalid = True

    invalid = True
    while invalid:
        invalid = False
        cycles = input("How many cycles would you like to repeat? ")
        try:
            cycles = int(cycles)
        except ValueError:
            print("That was not a valid number. Please try again. ")
            invalid = True

        if not invalid and cycles < 1:
            print("Please enter a time greater than 0.")
            invalid = True

    print("\n")
    work_time = tsec(work_time)
    rest_time = tsec(rest_time)
    pomodoro(work_time, rest_time, cycles)

    repeat = input("Would you like to continue studying? Enter 'y' to continue.")
    if repeat == 'y':
        cont = True
    else:
        cont = False
