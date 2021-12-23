# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  n+=1
tot = 0
for h in student_heights:
    tot += h
avg = round(tot / n)
print(f" The average of heights is {avg}" )
# 🚨 Don't change the code above 👆

    
#Write your code below this row 👇
