matrix = [1]
mynumber = 265149

even = 1
e = 0
while True:
    even = even+2
    #print(even)
    evensquare = (even)*(even)
    print("{} * {} = {}".format(even,even,evensquare))
    e += 1
    if evensquare >= mynumber:
         mylist = [e for e in range((even-2)*(even-2)+1,evensquare + 1)]
         mylist.reverse()
         print(mylist)
         print(e)
         print("first minimum index {}".format(e))
         print("second minimum index {}".format(e + (e*2)))
         print("third minimum index {}".format(e + (e*2)*2))
         print("fourth minimum index {}".format(e + (e*2)*3))
         mins = [abs(mylist[e]-mynumber),abs(mylist[e + (e*2)]-mynumber),abs(mylist[e + (e*2)*2]-mynumber),abs(mylist[e + (e*2)*3]-mynumber)]
         print(mins)
         print(min(mins)+e)

         break
