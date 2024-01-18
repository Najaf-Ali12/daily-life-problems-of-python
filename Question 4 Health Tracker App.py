#iiven by sir owais for mid preparation
#Question 4: Health Tracker App 
#Create a function check_activity_goal(steps_taken, goal)
#for a Health Tracker App. If the user has achieved their
#daily step goal (given as input), return "Goal achieved,"
#otherwise, provide a message indicating how many more
#steps are needed to reach the goal.
def check_activity_goals(x,y):
    if steps_taken==total_steps:
        if goal=="yes":
            print("congratulation,goal is acheived")
        else:
            print("check steps carefully and focus on goal")
    else:
        print("Fulfill remaining",remaining_steps,"steps to acheive the goal")
total_steps=int(input("enter the number of total steps patient has to take"))
steps_taken=int(input("enter the number of steps patient has taken"))
remaining_steps=total_steps-steps_taken
goal=input("enter,yes,if the goal is acheived,otherwise no")
check_activity_goals(steps_taken,goal)
