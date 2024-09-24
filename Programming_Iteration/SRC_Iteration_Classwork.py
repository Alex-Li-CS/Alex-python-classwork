C) 
average = round(total / 6, 1) 

D) 
temp = 0 
fever = 0 
total = 0 
hour = 1 
while hour < 7  
temp = input(“Enter temperature: ”) 
If temp<30 or temp > 40: 
Print("error invalid number") 
temp = input(“Enter temperature: ”) 
if temp > 37 then 
fever = fever + 1 
endif 
total = total + temp 
hour = hour + 1 
endwhile 
average = round(total/hour,1) #round to 1 decimal place 
print(“Average temperature:”, average) 
print(“Incidents of fever:”, fever) 
3) 
N = 0 
C = 0 
While True: 
part = int(input()) 
If len(str(part)) != 4: 
part = int(input()) 
Elif part == "9999": 
Break 
N += 1 
If part % 10 == 6 or part % 10 == 7 or part % 10 == 8: 
C += 1 
4) 
Loop always being true with not break 
Eg: i = 0  
while i < 10:  
print(i) 
  
5)  
Print("input test 1 scores for all students") 
Z = 0 
For x in range(0,30) 
Student = int(input()) 
Z += Student 
Average = Z // 30 
Print(Average) 

Print("input test 2 scores for all students") 
y= 0 
For x in range(0,30) 
Student = int(input()) 
y+= Student 
Average = y // 30 
Print(Average) 

 

 

Print("input test 3 scores for all students") 

d= 0 

For x in range(0,30) 

Student = int(input()) 

d+= Student 

Average = d // 30 

Print(Average) 

 

6) 

While True: 

Light =  "HIGH" 

pause(random(10, 100) 

light = LOW    

pause(random(10, 100)) 