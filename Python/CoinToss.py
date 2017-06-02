import random

def toss(res):
    print "Starting program"
    toss_count = 1
    heads_count = 0
    tails_count = 0
    results = ""
    toss_completed = ""

    for x in range (1, res):
        new_toss = random.randint(0,1)
        if new_toss == 1:
            heads_count +=1
            results = "Heads"
            print "Toss number", toss_count," Throwing coin now... It landed on", results+"! You have ", heads_count, "Heads and ", tails_count, "Tails"
        else:
            tails_count += 1
            results = "Tails"
            print "Toss number", toss_count," Throwing coin now... It landed on", results+"! You have ", heads_count, "Heads and ", tails_count, "Tails"
        toss_count += 1
toss(5001)
