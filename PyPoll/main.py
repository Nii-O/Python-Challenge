import os
import csv
import numpy as np

election_csv= os.path.join("Resources","election_data.csv")

voter_ID= []
county= []
candidates=[]
candidate= []

with open(election_csv, newline='', encoding= 'utf-8') as csvfile:
    csvreader= csv.reader(csvfile, delimiter= ',')
    for row in csvreader:

        voter_ID.append(row[0])
        county.append(row[1])
        candidates.append(row[2])

    total_votes= len(voter_ID)

    for name in candidates:
        if name not in candidate:
            candidate.append(name)


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


    

    per_khan= "{:.3%}".format(Khan_count/total_votes)
    per_correy= "{:.3%}".format(Correy_count/total_votes)
    per_li= "{:.3%}".format(Li_count/total_votes)
    per_otooley= "{:.3%}".format(Otooley_count/total_votes)


    #print(per_otooley)      
    #print(per_li)   


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
    #f"Winner: {greatest_decrease_date} \n"
    )

# Print the output (to terminal)
    print(output)



with open('PyPoll.txt','w') as final:
    
    
    final.write(output)

