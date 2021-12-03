import sys
txtfile = sys.argv[1]
people = sys.argv[2]

dict_data = {}
with open(txtfile,"r",encoding="utf-8") as data:
    for line in data:
        name = line.split(":")[0]
        dict_data[name] = (line.split(":")[1].split(","))

for person in people.split(","):
    try:
        print(f"Name: {person}, University:{dict_data[person][0]}, Department: {dict_data[person][1]}")
    except KeyError:
        print(f"No record of {person} was found!")

