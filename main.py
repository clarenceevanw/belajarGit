indonesiaGoal = 2
bahrainGoal = 1
time = 90
while(bahrainGoal != indonesiaGoal):
    time+=1
    print(time)
    print("Bahrain: ", bahrainGoal)
    print("Indonesia: ", indonesiaGoal)
    if(time == 99):
        bahrainGoal +=1
        print("Draw")
        print("Bahrain: ", bahrainGoal)
        print("Indonesia: ", indonesiaGoal)
        break


