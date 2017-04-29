var pay = 0.005;
var sum = 0;

for (var days = 1; days < 31; days = ++days)
{
  pay = pay*2;
  console.log("Day",days,"pay is:",pay);
  sum = pay*2;
}
console.log("In total the reward is:",sum);

// 10,000.00
var days =0;
for(var pay =0.01; pay < 10000.00; pay = pay*2)
{
  days = ++days;
}
console.log("This is how many days it takes to make reward goal",pay,"Days:",days);

//1 billion
var days =0;
for(var pay =0.01; pay < 1000000000.00; pay = pay*2)
{
  days = ++days;
}
console.log("This is how many days it takes to make reward goal",pay,"Days:",days);

//Infinity
var days =0;
for(var pay =0.01; pay < Infinity; pay = pay*2)
{
    days = ++days;
}
console.log("This is how many days it takes to make reward goal",pay,"Days:",days);
