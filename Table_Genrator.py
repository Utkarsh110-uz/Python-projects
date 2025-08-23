# Table Generator:

# This code generates tables from the number specific number to the number you want:

def tabelegenerator(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n * i}\n"

    with open(f"Tables/table_{n}.txt", "w") as f:
        f.write(table)
a = int(input("Enter number: "))
b = int(input("Enter number: "))
for i in range(a, b+1):
    tabelegenerator(i)
# For result please check the Tables folder 

# This code generates the table of the only number given by the user:

n = int(input("Enter nuber: "))
table = ""
for i in range(1, 11):
    table += f"{n} X {i} = {n * i}\n"

with open(f"Table/tabel_{n}.txt", "w") as f:
    f.write(table)
# For result please check the Table folder