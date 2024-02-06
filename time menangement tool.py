#Time Management Tool: Develop a tool to track time spent on various activities.
#Use variables to store task names and durations. Write expressions to calculate 
#total time spent on each task and identify areas for improvement.
list1=[]
sum=0
reply=input("enter whether you want to add more tasks in the list(yes/no)")
while reply.lower()=="yes" or reply.lower()=="add":
    task=input("enter the name of task:")
    duration=int(input(f"enter the total time spent on {task} in minutes:"))
    print("total time spent on",task,"is",duration)
    if duration<60:
        print(task,"requires extra time for improvement")
    else:
        print(duration,"is enough for",task,"keep working like this")
    list1.append(task)
    list1.append(duration)
    reply=input("enter whether you want to add more tasks in list,(yes/no)")
else:
    pass
print("the final list of tasks and duration on each task is ",list1)