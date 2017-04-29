var daysUntilMyBirthday = 60;

for (var daysUntilMyBirthday = 60; daysUntilMyBirthday > 0; daysUntilMyBirthday = daysUntilMyBirthday - 1)
{
  if(daysUntilMyBirthday > 30)
  {
    console.log(daysUntilMyBirthday,"days until my birthday. It is taking too long...");
  }
  else if (daysUntilMyBirthday <= 30 && daysUntilMyBirthday > 5)
  {
    console.log(daysUntilMyBirthday,"days until my birthday, It is getting closer.");
  }
  else if (daysUntilMyBirthday <= 5)
  {
    console.log(daysUntilMyBirthday,"DAYS UNTIL MY BIRTHDAY, I AM SO EXCITED!!!");
  }
}
console.log("IT'S MY BIRTHDAY!!!!!");
