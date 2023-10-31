#!/usr/bin/env python3

#Create a list
my_list = [ "192.168.0.5", 5060, "UP" ]

#Get the first value
print("The first item in the list (IP): " + my_list[0] )

#Get the second value
print("The second item in the list (port): " + str(my_list[1]) )

#Get the final item
print("The last item in the list (state): " + my_list[2] )

#Second list
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#Get IPs
print(iplist[3]+" and " +iplist[4])
