
import os
import csv

budget_data = os.path.join("budget_data.csv")

profits = []
net_change = []
months =[]

with open(budget_data, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    for row in csvreader:
    
        months.append(row[0])
        each_month = len(set(months))
        

        profits.append(int(row[1]))
        total_profits = sum(profits)
 

    for i in range(0,len(profits) -1): 

        net_change.append(int(profits[i+1]) - int(profits[i]))

    average_profits = sum(net_change)/len(net_change)


    greatest_increase = max(profits)
    greatest_decrease = min(profits)

    max_profit_date = months[profits.index(greatest_increase)]
    min_profit_date = months[profits.index(greatest_decrease)]

    print("Financial Analysis")
    print("---------------------------------")
    print(f"Total Number of Months: {str(each_month)}")
    print(f"Total: ${str(int(total_profits))}")
    print(f"Average Change: $ {str(int(average_profits))}" )
    print("Greatest Increase in Profits: " + str(max_profit_date) + " ($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + str(min_profit_date) + " ($" + str(greatest_decrease)+ ")")

with open("output.txt", "w") as x: 
   print("Financial Analysis \n", file = x)
   print("-----------------------------------\n", file=x)
   print(f"Total Number of Months: {str(months)}\n", file = x)  
   print(f"Total: ${str(int(total_profits))}\n", file = x)
   print(f"Average Change: $ {str(int(average_profits))}\n", file = x )
   print("Greatest Increase in Profits: " + str(max_profit_date) + " ($" + str(greatest_increase) + ")\n", file = x)
   print("Greatest Decrease in Profits: " + str(min_profit_date) + " ($" + str(greatest_decrease)+ ")\n", file = x)
