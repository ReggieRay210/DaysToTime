"""This program is created to allow the user to put in the desired number of 
days and convert those days to their corresponding minutes and hours."""

hours = 24
minutes = 60
m = "minutes"
hs = "hours"

calculation_to_minutes = hours * minutes


#   create a function
def days_to_time(number_of_days):
    return (f"{number_of_days} days are {number_of_days * calculation_to_minutes} { m} "
            f"and {number_of_days * hours} {hs}")


def check_and_execute():
    try:
        user_input_number = int(number_of_days_elements)
        if user_input_number > 0:
            time = days_to_time(user_input_number)
            print(time)
        elif user_input_number == 0:
            print("You Cannot Enter a Zero Day")
        else:
            print("You Cannot Go To The Past")
    except ValueError:
        print("Invalid Number Of Days")


print("Hello User, \n If you wondered how much time is spent from a single day, this program can help you figure that out.")
user_input = ""
while user_input != "exit":
    user_input = input("Enter the Number of Days you desire to Calculate: \n")
    for number_of_days_elements in set(user_input.split(',')):
        check_and_execute()
