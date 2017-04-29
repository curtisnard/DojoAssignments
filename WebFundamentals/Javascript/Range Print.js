function printRange(Start, Stop, Skip = 1)
{
  if(Stop === undefined)
  {
    Stop = Start;
    Start = 0;
  }
  for (var Start = Start; Start < Stop; Start += 1)
{
  if (Skip == 4 && Start % 4)
  {
    continue;
  }
  else if(Skip == 3 && Start % 3)
  {
    continue;
  }
  if(Skip == 2 && Start % 2)
  {
    continue;
  }

    console.log(Start);
  }
}

printRange(0,20, 4);
