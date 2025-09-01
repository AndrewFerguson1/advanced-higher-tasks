# Binary Search - Example 2


def initialise():
 searchlist = [10,15,25,26,60,90,100]
 print("Original list:",searchlist)
 return searchlist


def BinarySearch(searchlist,goal):
 found = False
 startpos = 0
 endpos = len(searchlist) -1
 comparisons = 0


 print ("Endpos at beginning = ",endpos)


 while (startpos <= endpos) and found == False:
     middle = (startpos+endpos)//2 #Integer Division
     comparisons+=1
     if searchlist[middle] == goal:
         found = True
     elif searchlist[middle]<goal:
         startpos = middle + 1
     else:
         endpos = middle -1


 if found == True:
   print("Match has been found at position",middle,"witihn",comparisons,"comparisons.")
 else:
   print(-1)


values = initialise()


goal = int(input("Enter goal: "))
BinarySearch(values,goal)
