str = "It's thanksgiving day. It's my birthday,too!"
print str.find("day")
newStr = str.replace("day","Month")
print newStr

x = [1,-3,0,10,-8]
max_val = max(x)
min_val = min(x)
print min_val
print max_val

x = ["curtis","hello",2,54,-2,7,12,98,"world","Nard"]
first = x[0]
last = x[-1]
print first
print last
new_x = first, last
print new_x

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
list_a = x[0:len(x)/2]
list_b = x[len(x)/2:len(x)]
list_b.insert(0,list_a)
print list_b
