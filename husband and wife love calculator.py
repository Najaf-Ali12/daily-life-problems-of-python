print("welcome to husband-wife love calculator")
husband=input("enter the name of husband:").lower()
wife=input("enter the name of wife:").lower()
count=0
vount=0
for i in husband:
    if i in "true":
        count+=1
for j in wife:
    if j in "true":
        count+=1
for k in wife:
    if k in "love":
        vount+=1
for l in husband:
    if l in "love":
        vount+=1
print("total love between the couple",husband," and ",wife," is",str(count)+str(vount),"percent")

