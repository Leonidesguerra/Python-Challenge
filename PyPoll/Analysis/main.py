import os
import csv

el_path = os.path.join ('..', 'Resources', 'election_data.csv')

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
    for x in poll:
        if x != i:
            candidate.append(x)
            i = x

    #count the votes per candidate and creating the list of results    
    for x in candidate:
        v_count.append(poll.count(x))

for x in range(len(candidate)):
    print(candidate[x], ' ', v_count[x])


    # s_results = sorted(results.items(), key=lambda item: item[1], reverse = True)


    # #obtain total votes
    # totalvotes = len(poll)

    # #print the data
    # print(f'```text\nElection Results')
    # print(f'---------------------------------------------')
    # print('Total Votes', totalvotes)
    # print(f'---------------------------------------------')
    # for x in s_results:
    #     print(f'{x[0]}: {round(x[1]/totalvotes*100, 2)}% ({x[1]})')
    # print(f'---------------------------------------------')
    # print(f'Winner: {s_results[0][0]}')
    # print(f'---------------------------------------------')
    # print(f'```')

    
       




# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```
# Voter ID,County,Candidate
# 12864552,Marsh,Khan
# 17444633,Marsh,Correy
# 19330107,Marsh,Khan
# 19865775,Queen,Khan