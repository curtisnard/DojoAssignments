var HOUR = 11;
var MINUTE =55;
var PERIOD ="PM";

if(MINUTE == 5)
{
  MINUTE ="5 after";
}
if(MINUTE == 15)
{
  MINUTE ="quarter after";
}
if(MINUTE == 30)
{
  MINUTE ="half past";
}
if(MINUTE == 45 && HOUR !=12 && HOUR !=11 )
{
  MINUTE ="quarter till";
  HOUR = HOUR+1;
}
if(MINUTE == 45 && HOUR ==11)
{
  MINUTE ="quarter till";
  HOUR = "midnight";
}
if(MINUTE == 45 && HOUR ==12)
{
  MINUTE ="quarter till";
  HOUR = HOUR-11;
}
if(MINUTE == 55 && HOUR !=12 && HOUR !=11 )
{
  MINUTE ="5 till";
  HOUR = HOUR+1;
}
if(MINUTE == 55 && HOUR ==11)
{
  MINUTE ="5 till";
  HOUR = "midnight";
}
if(MINUTE == 55 && HOUR ==12)
{
  MINUTE ="5 till";
  HOUR = HOUR-11;
}
if(MINUTE >0 && MINUTE < 5 || MINUTE >5 && MINUTE < 15)
{
  MINUTE = "just after";
  HOUR = HOUR;
}
if(MINUTE <=59 && MINUTE >55 || MINUTE <55 && MINUTE >45)
{
    MINUTE = "almost";
    HOUR = HOUR-11;
}
if(PERIOD =="AM")
{
  PERIOD = "in the morning";
}
if(PERIOD =="PM" && HOUR >0 && HOUR < 7)
{
  PERIOD = "in the afternoon";
}
if(PERIOD =="PM" && HOUR >6 && HOUR < 12)
{
  PERIOD ="at night";
}

if(PERIOD =="AM" && HOUR ==12 && MINUTE == 0 || PERIOD =="in the morning" && HOUR ==12 && MINUTE == 0)
{
  PERIOD ="midnight"
  console.log("It is",PERIOD);
}
else if(PERIOD == "PM" && HOUR ==12 && MINUTE == 0)
{
  PERIOD = "noon";
  console.log("It is ",PERIOD);
}
else if(HOUR == "midnight")
{
  console.log("It is",MINUTE, HOUR);
}
else if(MINUTE == MINUTE)
{
  console.log("It is",MINUTE, HOUR, PERIOD);
}
