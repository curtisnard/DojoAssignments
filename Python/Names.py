students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def Part1(x):
    for item in x:
        print item['first_name'],item['last_name']
Part1(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
def Part2(dictionary):
    for x in dictionary:
        y = 0
        print x
        for z in dictionary[x]:
            y += 1
            first_name = z['first_name']
            last_name = z['last_name']
            length = len(z['first_name'])+ len(z['last_name'])
            dash = " -"
            print "{} - {} {} - {}".format(y, z['first_name'],z['last_name'],length)
Part2(users)
