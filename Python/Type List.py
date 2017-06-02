def typeList(x):
    y = 0
    z = 0
    strs = ''
    ints = 0
    for item in x:
        if isinstance(item, str) == True:
            y += 1
            strs += item + ''
        else:
            z += 1
            ints += item
    if y and z > 0:
        print "Your entered list is a mixed type"
        print "String:", strs
        print "Sum:", ints
    elif y > 0 and z == 0:
        print "Your entered list is a String type"
        print "String:", strs
    else:
        print "Your entered list is an integer type"
        print "Sum:", ints

typeList(['magical unicorns ','Fairy Princess ','Queen ','Dragon'])
