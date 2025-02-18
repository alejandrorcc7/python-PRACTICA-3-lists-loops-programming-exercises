names = ['Esmeralda','Steven','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Pepe']

# Your code here
names[1] = "Steven"
names[-1] = "Pepe"
names[0] = names[2] + names[4]
for i in range(len(names) - 1, -1 , -1):
    print(names[i])
