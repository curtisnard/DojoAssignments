var game = 0;
var cashout = 0;
function slots(cashout =1000)
{
      console.log("Welcom to slots, Please insert one quarter and begin");
        for(var quarter = 20 ; quarter> 0; ++game)
        {
          var chance = Math.trunc(Math.random() * 100)+1;
        if(quarter == 0)
        {
          break;
        }
        else if (chance == 25)
        {
          var quartersWon = Math.floor(Math.random() * 50)+50;
          quarter= quarter+quartersWon;
          console.log("you have won",quartersWon,"quarters, you now have",quarter,"quarters");

        }
        else if(chance != 25)
        {
          quarter = quarter -1;
          console.log("Game",game,"Try Again",quarter,"quarters remaining");
        }
        if (quarter > cashout)
        {
          console.log("Thanks for playing, Please come again");
          break;
        }
        }


}
slots(200);
