def draw_stars(x):
    for item in x:
        print "*" * item
y = [1,2,3,4,3,2,1]

draw_stars(y)

def draw_stars2(x):
    for item in x:
        if isinstance(item, int):
            print "*" * item
        elif isinstance(item, str):
            #length = len(item)
            #letter = item[0].lower()
            print item[0].lower() * len(item)
y = [1,"me",2,"you",3]
draw_stars2(y)
