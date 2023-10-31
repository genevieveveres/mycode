#!/usr/bin/env python3

#create the original lists
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]

#display the original lists
print(proto)

#append "dns" to both lists
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list

#display the newly edited lists
print(proto)

#create a list of ints
proto2 = [ 22, 80, 443, 53 ] # a list of common ports

#test what extend does
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)

#test what append does
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)


#add one more method
protoa.clear()
print(protoa)
