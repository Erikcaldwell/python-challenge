import csv
# importing the CSV file into Python lists dates and profits
with open('budget_data.csv') as csvfile:
    importedCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    profits = []

# reading the list data into variables date and pl
    for row in importedCSV:
        date = row[0]
        pl = row[1]

#appending my dates and profits variables with the date and pl data
        dates.append(date)
        profits.append(pl)

#removing headers from list data.
monthYear = dates[1:len(dates)]
pAndL = profits[1:len(profits)]

# converting profits from a string to an int so I can do math
for i in range(len(pAndL)):
    pAndL[i] = int(pAndL[i])

# calulating the profit and loss totals
totalPL = sum(pAndL)

# calulating the total number of months in the data
months = 0
months = len(pAndL)

#calulating the average change in profits between months
pAndL2 = pAndL[1:len(pAndL)]
#stuff = 0
change = []
a = 0
for a in range(len(pAndL2)):
    #change[i] = pAndL[i]-pAndL2[i]
    #change.append(pAndL[a]-(pAndL2[a]))
    change.insert(i, pAndL[a]-pAndL2[a])
    changeSum = sum(change)
    changes = len(change)
    averageChange = round(changeSum / changes,2)*-1

#calulating the greatest increase and decrease increase

greatestIncrease = min(change)*-1
greatestDecrease = max(change)*-1
index1 = change.index(int(max(change)))+1
greatestMonth = monthYear[index1]
index2 = change.index(int(min(change)))+1
greatestMonth2 = monthYear[index2]

#outputs are hanging out here
print("Financial Analysis")
print("-------------------------------------")
print("Total Months: {num}".format(num=months))
print("Total: ${num}".format(num=totalPL))
print("Average Change: ${num}".format(num=averageChange))
print("Greatest Increase in Profits: {one} (${two})".format(one=greatestMonth, two=greatestIncrease))
print("Greatest Decrease in Profits: {one} (${two})".format(one=greatestMonth2, two=greatestDecrease))

#write results to the text file
text_file = open("pybank.txt", "w")
text_file.write("Financial Analysis")
text_file.write("\n")
text_file.write("-------------------------------------")
text_file.write("\n")
text_file.write("Total Months: {num}".format(num=months))
text_file.write("\n")
text_file.write("Total: ${num}".format(num=totalPL))
text_file.write("\n")
text_file.write("Average Change: ${num}".format(num=averageChange))
text_file.write("\n")
text_file.write("Greatest Increase in Profits: {one} (${two})".format(one=greatestMonth, two=greatestIncrease))
text_file.write("\n")
text_file.write("Greatest Decrease in Profits: {one} (${two})".format(one=greatestMonth2, two=greatestDecrease))
text_file.write("\n")
text_file.close()
