import os
import csv
import numpy as np

pybank_csv= os.path.join("Resources","budget_data.csv")

date= []
pl= []
pl_int=[]

with open(pybank_csv, newline='', encoding= 'utf-8') as csvfile:
    csvreader= csv.reader(csvfile, delimiter= ',')
    for row in csvreader:

        date.append(row[0])

        pl.append(row[1])

    date.pop(0)
    pl.pop(0)

    for i in range(0, len(pl)):
        pl_int.append(int(pl[i]))


    total_month= len(date)
    total=0
    for num in pl_int:
        total+= num
    

    difference= np.diff(pl_int)
    avgchange= difference.sum()/len(difference)
    
    maximum= max(pl_int)
    max_date_index= pl_int.index(maximum)
    max_date= date[max_date_index]

    minimum= min(pl_int)
    min_date_index= pl_int.index(minimum)
    min_date= date[min_date_index]

    report1= (
    print("__________Financial Analysis__________"),
    print("Total Months:                    " +str(total_month)),
    print('Total:                           '+ '$'+str(total)),
    print('Average Change:                  '+'$'+str(avgchange)),
    print('Greatest Increase in Profits:    '+ max_date+ '  $'+str(maximum)),
    print('Greatest Decrease in Profits:    '+ min_date+ '  $'+str(minimum)))
    
    print(report1)

    output = (
    f"Financial Analysis\n"
    f"------------------------------------------------------------\n"
    f"Total Months:                     {total_month}\n"
    f"Total:                            ${total}\n"
    f"Average  Change:                  ${avgchange:.2f}\n"
    f"Greatest Increase in Profits:     {max_date} (${maximum})\n"
    f"Greatest Decrease in Profits:     {min_date} (${minimum})\n")

    print(output)
    


with open('PyBank.txt','w') as final:
    
    
    final.write(output)



















#test_zip= zip(date, pl)

#output_file = os.path.join("test_final")

#with open(output_file, "w", newline="") as datafile:
 #   writer = csv.writer(datafile)

  #  writer.writerow(["Date","Profit/Loss"])

   # writer.writerows(test_zip)

