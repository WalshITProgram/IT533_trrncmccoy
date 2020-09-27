Matter_of_Time = ["My Profile", "RoadSide Assistance", "Rewards"]
Profile_policy = ["My Policy", "Schedule a Appointment", "My Car Report", "My Repair Status", "My Payment"]

print("Checking for profile")
for n in Profile_policy:
    print(n)
    if n == "My Car Report":
        break
    
print("End of Search")

Plan_1 = 300
Plan_2 = 200
Plan_3 = 100
plan_price = [300, 200, 100]

for i in plan_price:
    if i <= 100: 
        print(Plan_1)
        
    if i <= 200:
        print(Plan_2)

    if i <= 300:
        print(Plan_3)

index = [] 

while len(Profile_policy) == 5:
    client = Profile_policy.pop(0)
    index.append(client)
    print(index)

Package_price = [[300, 200, 100], [50, 25, 10], [5, 2,0]]
My_Profile = 0
for x in Package_price:
    print(x)
    for s in x:
        My_Profile += s
       
        print(My_Profile)

username = ["Jay Rock", "Schoolboy Q", "Kendrick Lamar", "Ab Soul"]

usernames = [user for user in username if user == "Jay Rock"]
TDE_1 = [user + " Talk that Talk" for user in usernames]
print(TDE_1)
print(usernames)

single_digits = range(9)
sqaures = []
for i in single_digits:
        sqaures.append(i**2)
        print(i)
cubes = [i**2 for i in single_digits]
print(cubes)