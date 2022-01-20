#import the needed packages
import os
import csv
import numpy as np

#creating the path to the csv file
pybank_csv= os.path.join("Resources","budget_data.csv")

#create three empty lists to store the contents of the  each column in the csv
date= []
pl= []
pl_int=[]

#open the csv file and storing the columns in the empty lists date and pl
with open(pybank_csv, newline='', encoding= 'utf-8') as csvfile:
    csvreader= csv.reader(csvfile, delimiter= ',')
    for row in csvreader:

        date.append(row[0])

        pl.append(row[1])

    #removing the first entry from each list since that entry is just the column names (Date & Profit/Loss).
    date.pop(0)
    pl.pop(0)

    #converting the strings in the pl list to int and storing them in a different list pl_int
    for i in range(0, len(pl)):
        pl_int.append(int(pl[i]))

    #calculating the total nuber of months
    total_month= len(date)
    total=0

    #calculating the net total amount of "Profit/Loss" over the entire period
    for num in pl_int:
        total+= num
    
    #calculating the changes in "Profit/Loss" over the entire period. 
    #Used numpy to find the difference between consecutive numbers which is stored as a list in 'difference'
    #The changes in "Profit/Loss" is the sum of 'difference list' divided by the length of the list
    difference= np.diff(pl_int)
    avgchange= difference.sum()/len(difference)
    
    #Found the max profit from the 'pl_int' list then used '.index' to find the position of this value.
    #The position of the max profit is stored in 'max_date_index' which is later used to pull the corresponding date to this max value from the 'date' list.
    maximum= max(pl_int)
    max_date_index= pl_int.index(maximum)
    max_date= date[max_date_index]

    #Found the min profit from the 'pl_int' list then used '.index' to find the position of this value.
    #The position of the min profit is stored in 'min_date_index' which is later used to pull the corresponding date to this min value from the 'date' list.
    minimum= min(pl_int)
    min_date_index= pl_int.index(minimum)
    min_date= date[min_date_index]

    
    #Storing all print statements to the variable output and later pringting that to the terminal
    output = (
    f"Financial Analysis\n"
    f"------------------------------------------------------------\n"
    f"Total Months:                     {total_month}\n"
    f"Total:                            ${total}\n"
    f"Average  Change:                  ${avgchange:.2f}\n"
    f"Greatest Increase in Profits:     {max_date} (${maximum})\n"
    f"Greatest Decrease in Profits:     {min_date} (${minimum})\n")

    print(output)
    

#creating a new text file to store the analysis in the 'Analysis' folder

output_path = os.path.join('..','Analysis','PyBank.txt')


with open(output_path,'w') as final:
    
    final.write(output)













#test_zip= zip(date, pl)

#output_file = os.path.join("test_final")

#with open(output_file, "w", newline="") as datafile:
 #   writer = csv.writer(datafile)

  #  writer.writerow(["Date","Profit/Loss"])

   # writer.writerows(test_zip)

