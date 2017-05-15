#Multiples
#Part 1
for count in range(0,1001):
    if count %2==0:
        continue
    print "odd numbers", count
#part 2
for count in range(5,1000000, 5):
    print "Multiples of 5", count
#Sum List
a = [1,2,5,10,255,3]
print sum(a)
#Average List
a = [1,2,5,10,255,3]
print sum(a)/float(len(a))
