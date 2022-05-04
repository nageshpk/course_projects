from datetime import datetime

#user input
user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
print(deadline_date)
print(type(deadline_date))

today_date = datetime.today()

time_till = deadline_date - today_date

print(f'Dear user! Time remaining for your goal is: {goal} is {time_till.days} days')