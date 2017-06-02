def odd_even():
    for num in range(1, 2001):
        if num %2 == 0:
            print num, " This is an even number"
        else:
            print num, " This is an odd number"
odd_even()
def multiply(list, num):
    for item in range(0,len(list)):
        list[item] *= num
    return list
mult_list = [5,10,15,20]
print multiply(mult_list,5)
def layered_multiples(a):
    print a
    new_a = []
    for item in a:
        temp_a=[]
        for item2 in range(0,item):
            temp_a.append(1)
        new_a.append(temp_a)
    return new_a
item = layered_multiples(multiply([2,4,5],3))
print item
