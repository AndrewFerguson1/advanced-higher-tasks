data = ["G","X","b","P","z"]

for index in range(1,len(data)):
    currentvalue = ord(data[index])
    position = index


    while position > 0 and ord(data[position-1])>currentvalue:
        data[position]