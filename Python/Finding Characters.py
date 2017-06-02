str = ['hello','world','my','name','is','Curtis']
char = 's'
selectchar= ''
newstr = []
for item in str:
    selectchar = item.find(char)
    if (selectchar >= 0):
        newstr.append(item)
print newstr
