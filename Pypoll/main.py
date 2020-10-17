

import os
import csv


electionData = os.path.join("election_data.csv")

electees = []

voteCounter = []

votePercentages = []

voteTotal = 0

with open(electionData, newline = "") as csvfile:
        csvread = csv.reader(csvfile, delimiter = ",")
        header = next(csvread)
        for row in csvread:
       
            voteTotal += 1 
        
            if row[2] not in electees:
                electees.append(row[2])
                index = electees.index(row[2])
                voteCounter.append(1)
        
            else:
                index = electees.index(row[2])
                voteCounter[index] += 1
    
    
        for voteNumber in voteCounter:
            percentage = (voteNumber / voteTotal) * 100
        
            percentage = round(percentage)
        
            percentage = "%.3f%%" % percentage
        
            votePercentages.append(percentage)
    
    
        highestVoteIndex = voteCounter.index(max(voteCounter))
   
        winner = electees[highestVoteIndex]


        print("Election Results")
        print("------------------------------")
        print(f"Total Votes: {str(voteTotal)}")
        print("------------------------------")
        for i in range(len(electees)):
            print(f"{electees[i]}: {str(votePercentages[i]) } ({str(voteCounter[i])})")
        print("------------------------------")
        print(f"Winner: {winner}")
        print("------------------------------")


with open("output.txt", "w") as x: 
   print("Election Results \n", file = x)
   print("------------------------------\n", file=x)
   print(str(f'Total Votes: {str(voteTotal)}\n'), file = x)
   print("------------------------------\n", file = x)
   for i in range(len(electees)):
        print(str(f'{electees[i]}: {str(votePercentages[i])} ({str(voteCounter[i])})'), file = x)
   print("------------------------------\n", file = x)
   print(str(f'Winner: {winner}\n'), file = x)
   print("------------------------------\n", file = x)