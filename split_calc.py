#Function if I am being Greedy
def risky_bet():
    print('THIS IS FOR BETTING ON THE RISKY TEAM')
    #Setting Variables
    betMoney = float(input("What is the total amount you wish to bet: "))
    OddLower = float(input("What is the odds lower odds of the 2 teams: "))
    #OddHigher = float(input("What is the odds higher odds of the 2 teams: "))
    
    #Calcualtions
    lowerBet = betMoney/(OddLower + 1)
    moneyMade = round((betMoney - lowerBet) - lowerBet*OddLower, 2) 

    #Analysis
    if moneyMade >= 0.00:
        print("If this test displays 0.0, calculations were correct: " + str(moneyMade))
         
    print("You should bet " + str(lowerBet) + " On the Team with lower odds and rest on the other.")
    
        
def safe_bet():
    print('\n \nTHIS IS FOR BETTING ON THE SAFE TEAM')
    #Setting Variables
    betMoney = float(input("What is the total amount you wish to bet: "))
    #OddLower = float(input("What is the odds lower odds of the 2 teams: "))
    OddHigher = float(input("What is the odds higher odds of the 2 teams: "))
    
    #Calculations
    higherBet = betMoney/(OddHigher + 1)
    moneyMade = round((betMoney - higherBet) - higherBet*OddHigher, 2) 

    #Analysis
    if moneyMade >= 0.00:
        print("If this test displays 0.0, calculations were correct: " + str(moneyMade))
    
    print("You should bet " + str(higherBet) + " On the Team with HIgher odds and rest on the other.")
    
safe_bet()
