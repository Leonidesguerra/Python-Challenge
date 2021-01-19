import os
import csv

budget_path = os.path.join('..', 'Resources', 'budget_data.csv')
analysis_path = os.path.join("..", "Analysis", "analysis.txt")

month = [] #lis created with the month column
change =[] #list created with the montly profit change
profit = {}

netprofit = 0
prev = 0 # this will be used to use the previous profit value in order to calculate the change
tch = 0
ginc = 0
gdec = 0
diff = 0

with open(budget_path) as budgetfile:
    dataset = csv.reader(budgetfile, delimiter=',')
    csv_header = next(dataset)
  
   #generate the list called month
   #obtain the net profit by adding all the values on the list
    for row in dataset:
        month.append(row[0])
        netprofit += int(row[1])
      
       #calculate the change value. Since the the first value does not have a previous value change will be 0
        if prev == 0:
            change.append(0)
        else:
            diff =  int(row[1]) - prev
            change.append(diff)
       
        prev = int(row[1])

    for x in range(len(month)):  
        profit[month[x]]= change[x]

#obtain greatest and lowest profit values    
gic = max(profit, key=profit.get)
gdec = min(profit, key=profit.get)


#calculate the average change
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
print (f'Greatest Increase in Profits: {gic} ({profit[gic]})')
# The greatest decrease in losses (date and amount) over the entire period
print (f'Greatest Decrease in Profits: {gdec} ({profit[gdec]})')

with open(analysis_path, 'w') as textfile:
    textfile.write(f'Total Months: {len(month)}\n')
    textfile.write (f'Net Profit: ${netprofit}\n')
    textfile.write(f'Average change: ${round(avch,2)}\n')
    textfile.write(f'Greatest Increase in Profits: {gic} ({profit[gic]})\n')              
    textfile.write(f'Greatest Decrease in Profits: {gdec} ({profit[gdec]})\n')