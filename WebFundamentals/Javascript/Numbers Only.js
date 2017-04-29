var myArray = function numbersOnly(nums)
{
  var storage =[];
  for (var i = 0; i <nums.length; ++i)
  {
    if (typeof nums[i]==="number")
    {
      storage.push(nums[i]);
    }
  }
  return storage;
}

var newArray = myArray([1,"little",2,"lil",3,"lilIndians"]);

console.log(newArray);
