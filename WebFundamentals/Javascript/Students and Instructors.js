var users = {
'Students' : [
    {
      first_name : 'Michael',
      last_name : 'jordan'
    },
    {
      first_name : 'John',
      last_name : 'Rosales'
    },
    {
      first_name : 'Mark',
      last_name : 'Guillen'
    },
    {
      first_name : 'KB',
      last_name : 'Tonel'
    }
  ],
'Instructors': [
    {
      first_name : 'Michael',
      last_name : 'Choi'
    },
    {
      first_name : 'Martin',
      last_name : 'Puryear'
    }
  ]
}
console.log("Students");
for (i = 0; i < users.Students.length; ++i)
{
  var dash = " -"
  console.log(i+1 +dash, users.Students[i].first_name, users.Students[i].last_name +dash , users.Students[i].first_name.length+users.Students[i].last_name.length);
}
console.log("Instructors");
for(j = 0; j < users.Instructors.length; ++j)
{
  var dash = " -"
  console.log(j+1 +dash,users.Instructors[j].first_name,users.Instructors[j].last_name +dash,users.Instructors[j].first_name.length+users.Instructors[j].last_name.length);
}
