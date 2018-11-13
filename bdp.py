# bdp.py
# calculate bandwidth delay product of a link using bits/sec and seconds
# seconds can be entered as decimals as they will be read in as a floating point variable


bandwidth = int(input("Enter the link bandwidth in bits/sec: "))

delay = float(input("Enter the Round Trip Time in seconds: "))

bdp = (bandwidth * delay) / 8

print("The Bandwidth Delay Product of this link is: " + str(bdp) + "bytes" )
