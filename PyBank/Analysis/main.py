import os
import csv

budget_path = os.path.join('..', 'Resources', 'budget_data.csv')
months = 0
netprofit = 0
prev = 0
change =[]
tch = 0
ginc = 0
gdec = 0
diff = 0
with open(budget_path) as budgetfile:
    dataset = csv.reader(budgetfile, delimiter=',')
    csv_header = next(dataset)
   

    for row in dataset:
        # create a dictionary withs months : change instead 
        
        months += 1
        netprofit += int(row[1])
       
        if prev == 0:
            change.append(0)
        else:
            diff = prev - int(row[1])
            change.append(diff)
        # if diff < 0:
        #     if diff < gdec:
        #         gdec=dif

        prev = int(row[1])

    




nch = len(change)-1
for x in change: 
    tch += int(x)
    
avch = tch / nch





#The total number of months included in the dataset
print(f'Total Months: {months}')

#The net total amount of "Profit/Losses" over the entire period
print (f'Net Profit: {netprofit}')
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
print(f'Average change: {avch}')
#The greatest increase in profits (date and amount) over the entire period
#
# The greatest decrease in losses (date and amount) over the entire period