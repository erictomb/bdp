# bdp.py
# calculate bandwidth delay product of a link

bandwidth = int(input("Enter the link bandwidth in bits/sec: "))

delay = float(input("Enter the Round Trip Time in seconds: "))

bdp = (bandwidth * delay) / 8

print("The Bandwidth Delay Product of this link is: " + str(bdp) + "bytes" )
