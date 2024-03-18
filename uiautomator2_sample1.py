import uiautomator2 as u2

#d = u2.connect("127.0.0.1:5555") # connect to device
d = u2.connect() # connect to device
print(d.info)