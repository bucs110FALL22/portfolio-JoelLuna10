import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
#Added
class_per_week = 5
cost_per_class = ((cost_per_week)/(class_per_week))
print("Cost per class:", cost_per_class)
#-----
print(class_per_week, type(class_per_week))
print(cost_per_class, type(cost_per_class))



#Part B
#Added
print(random.randrange(1,10))
l = [5,"s",0.4,6,"r"]
print(str(random.choice(l)) + " yes")
#-----
