# Insertion sort

#list = [1,2,6,8,5,32,2,5,8,8,65,4,3,3,4,7,9,9,7,54,32,345,678,9,87,654,32,34,5678,9,8,7654,32,345,678,87,654,32]

list = [352,976,3125,54224,475,85,6497,1,5,9,2,58346,35985854577,4342547,1]

print(f"The unordered list is {list}.")

for i in range (len(list)):
    value = list[i]
    position = i
    while position>0 and (list[position-1]>value):
        list[position] = list[position-1]
        position-=1
    list[position] = value

print(f"The ordered list is {list}.")