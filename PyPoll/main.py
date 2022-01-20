#import the needed packages
import os
import csv
import numpy as np

#creating the path to the csv file
election_csv= os.path.join("Resources","election_data.csv")

#create three empty lists to store the contents of the  each column in the csv and one extra list to store 'integers'
voter_ID= []
county= []
candidates=[]
candidate= []

#open the csv file and storing the columns in the empty lists 'voter_ID', 'county' and 'candidates'
with open(election_csv, newline='', encoding= 'utf-8') as csvfile:
    csvreader= csv.reader(csvfile, delimiter= ',')
    for row in csvreader:

        voter_ID.append(row[0])
        county.append(row[1])
        candidates.append(row[2])

    #removing the first entry from each list since that entry is just the column names
    voter_ID.pop(0)
    county.pop(0)
    candidates.pop(0)


    #find the length of any column to see the number of people that voted
    total_votes= len(voter_ID)

    # I created a seprate list to store the names of the candidates who ran for the position
    for name in candidates:
        if name not in candidate:
            candidate.append(name)

# I used for loops to count the number of times a candidates name appered in the 'candidates' list to get the total votes for that candidate
    Khan_count=0
    for i in candidates:
        if i== 'Khan':
            Khan_count+= 1

    Correy_count=0
    for j in candidates:
        if j== 'Correy':
            Correy_count+= 1

    Li_count=0
    for k in candidates:
        if k== 'Li':
            Li_count+= 1

    Otooley_count=0
    for l in candidates:
        if l== "O'Tooley":
            Otooley_count+= 1


    
   # Calculating the percentage of votes each candidate had and formatting that number to a percentage with three decimal places.
    per_khan= "{:.3%}".format(Khan_count/total_votes)
    per_correy= "{:.3%}".format(Correy_count/total_votes)
    per_li= "{:.3%}".format(Li_count/total_votes)
    per_otooley= "{:.3%}".format(Otooley_count/total_votes)

   #finding the winner from a list of total votes usinf if statements to find the max ot the 'winner_list'.
    winner_list= [Khan_count, Correy_count, Li_count, Otooley_count]
    winner=""
    for val in winner_list:
        if max(winner_list) is Khan_count:
            winner= 'Khan'
        elif max(winner_list) is Correy_count:
            winner= 'Correy'
        elif max(winner_list) is Li_count:
            winner= 'Li'
        elif max(winner_list) is Otooley_count:
            winner= "O'Tooley"


    #Storing all print statements to the variable output and later pringting that to the terminal
    output = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n"
    f"Khan:       {per_khan} ({Khan_count})\n"
    f"Correy:     {per_correy} ({Correy_count})\n"
    f"Li:         {per_li} ({Li_count})\n"
    f"O'Tooley:   {per_otooley} ({Otooley_count})\n"
    f"----------------------------\n"
    f"Winner:     {winner} \n"
    f"----------------------------\n"
    )

# Print the output (to terminal)
    print(output)


#creating a new text file to store the analysis in the 'Analysis' folder
output_path = os.path.join('..','Analysis','PyPoll.txt')
with open(output_path,'w') as final:
    final.write(output)
