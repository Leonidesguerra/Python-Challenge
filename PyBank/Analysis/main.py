import os
import csv

budget_path = os.path.join('..', 'Resources', 'budget_data.csv')
month = []

change =[]
netprofit = 0
prev = 0

tch = 0
ginc = 0
gdec = 0
diff = 0
with open(budget_path) as budgetfile:
    dataset = csv.reader(budgetfile, delimiter=',')
    csv_header = next(dataset)
   

    for row in dataset:
        month.append(row[0])
        netprofit += int(row[1])
       
        if prev == 0:
            change.append(0)
        else:
            diff =  int(row[1]) - prev
            change.append(diff)
       
        prev = int(row[1])

    
gic = max(change)
gdec = min(change)

i= change.index(gic)
j= change.index(gdec)



nch = len(change)-1
for x in change: 
    tch += int(x)
    
avch = tch / nch





#The total number of months included in the dataset
print(f'Total Months: {len(month)}')

#The net total amount of "Profit/Losses" over the entire period
print (f'Net Profit: ${netprofit}')
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
print(f'Average change: ${round(avch,2)}')
#The greatest increase in profits (date and amount) over the entire period
print (f'Greatest Increase in Profits: {month[i]} ({gic})')
# The greatest decrease in losses (date and amount) over the entire period
print (f'Greatest Decrease in Profits: {month[j]} ({gdec})')