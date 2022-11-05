values = [1, 2, "test", 4, 5]

print(values[2])   #1

print(values[-1]) # Print last value of the list

print(values[1:3]) # print to begin index to last index-1 value

values.insert(3, "M") # insert element to specific index of a list

print(values)
values.append("end") # add the value at the last index
print(values)

values[2]="TEST" # updating value

del values[0]

print(values)

val = (1, 2, "LOkesh", "4.5")

#val[2] = "LOKESH"
print(val)

#Dictionary

dic = {"a": 2, 3: "bcd", "c": "Hello World"}

print(dic[3])

print(dic["c"])

# Dictionary creation at run time

dict = {}

dict["firstName"] = "Lokesh"
dict["lastName"] = "M"
dict["Gender"] = "Male"
print(dict)
print(dict["lastName"])
