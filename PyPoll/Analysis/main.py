import os
import csv

el_path = os.path.join ('..', 'Resources', 'election_data.csv')
analysis_path = os.path.join ('..', 'Analysis', 'election_Results.txt')

poll = [] #list formed with candidate column (vote per voter id)
candidate = [] #list of candidates which received a vote
v_count =[]
results = {}
vote_percentage =[]
i = ' '
#read file and skip the keader
with open(el_path) as eldata:
    election = csv.reader(eldata, delimiter=',')
    csv_header = next(election)
    
    #create a list with tha candidate column, because the other data is not relevant for the result
    for row in election:
           poll.append(row[2])
    
    #by sorting the data, in order to create a list of candidates who received votes
    poll.sort()
    for x in poll:
        if x != i:
            candidate.append(x)
            i = x

    #count the votes per candidate and creating a dictionary witn candidate and the number of votes per candidate    
    for y in candidate:
         results[y] = poll.count(y)

    #sorting the dictionary from greater to lower   
    s_results = sorted(results.items(), key=lambda item: item[1], reverse = True)

    #obtain total votes
    totalvotes = len(poll)

    #print the data
    print(f'```text\nElection Results')
    print(f'---------------------------------------------')
    print('Total Votes: ', totalvotes)
    print(f'---------------------------------------------')
    for x in s_results:
        print(f'{x[0]}: {round(x[1]/totalvotes*100, 2)}% ({x[1]})')
    print(f'---------------------------------------------')
    print(f'Winner: {s_results[0][0]}')
    print(f'---------------------------------------------')
    print(f'```')

    with open(analysis_path, 'w') as textfile:
        
        textfile.write(f'```text\nElection Results\n')
        textfile.write(f'---------------------------------------------\n')
        textfile.write(f'Total Votes: {totalvotes}\n')
        textfile.write(f'---------------------------------------------\n')
        for x in s_results:
            textfile.write(f'{x[0]}: {round(x[1]/totalvotes*100, 2)}% ({x[1]})\n')
        textfile.write(f'---------------------------------------------\n')
        textfile.write(f'Winner: {s_results[0][0]}\n')
        textfile.write(f'---------------------------------------------\n')
        textfile.write(f'```\n')