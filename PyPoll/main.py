import csv
from decimal import Decimal
# importing the CSV file into Python
with open('election_data.csv') as csvfile:
    importedCSV = csv.reader(csvfile, delimiter=',')
    voterID_dirty = []
    county_dirty = []
    candidate_dirty = []

# reading the list data into variables date and pl
    for row in importedCSV:
        voter = row[0]
        place = row[1]
        who = row[2]

#appending
        voterID_dirty.append(voter)
        county_dirty.append(place)
        candidate_dirty.append(who)

#removing headers from list data.
voterID = voterID_dirty[1:len(voterID_dirty)]
county = county_dirty[1:len(county_dirty)]
candidate = candidate_dirty[1:len(candidate_dirty)]

#calulating total votes cast
totalVotes = len(candidate)

#creating a list of candidates
candidateList=list(set(candidate))

#creating vote tallies
candidate0Votes=candidate.count(candidateList[0])
candidate1Votes=candidate.count(candidateList[1])
candidate2Votes=candidate.count(candidateList[2])
candidate3Votes=candidate.count(candidateList[3])

#creating vote percentages
candidate0Per = Decimal(candidate0Votes/totalVotes*100)
candidate1Per = Decimal(candidate1Votes/totalVotes*100)
candidate2Per = Decimal(candidate2Votes/totalVotes*100)
candidate3Per = Decimal(candidate3Votes/totalVotes*100)
candidate0PerDes = round(candidate0Per,3)
candidate1PerDes = round(candidate1Per,3)
candidate2PerDes = round(candidate2Per,3)
candidate3PerDes = round(candidate3Per,3)

#picking, i mean determining the winner
wlist = []
wlist.append(candidate0Votes)
wlist.append(candidate1Votes)
wlist.append(candidate2Votes)
wlist.append(candidate3Votes)
BW= wlist.index(int(max(wlist)))
winner= candidateList[BW]

#outputs are hanging out here
print("Election Results")
print("------------------------------")
print("Total Votes: {num}".format(num=totalVotes))
print("------------------------------")
print("{one}: {two}% ({three})".format(one=candidateList[0], two=candidate0PerDes, three=candidate0Votes))
print("{one}: {two}% ({three})".format(one=candidateList[1], two=candidate1PerDes, three=candidate1Votes))
print("{one}: {two}% ({three})".format(one=candidateList[2], two=candidate2PerDes, three=candidate2Votes))
print("{one}: {two}% ({three})".format(one=candidateList[3], two=candidate3PerDes, three=candidate3Votes))
print("------------------------------")
print("Winner: {str}".format(str=winner))
print("------------------------------")


#write results to the text file
text_file = open("results.txt", "w")
text_file.write("Election Results")
text_file.write("\n")
text_file.write("------------------------------")
text_file.write("\n")
text_file.write("Total Votes: {num}".format(num=totalVotes))
text_file.write("\n")
text_file.write("\n")
text_file.write("------------------------------")
text_file.write("\n")
text_file.write("{one}: {two}% ({three})".format(one=candidateList[0], two=candidate0PerDes, three=candidate0Votes))
text_file.write("\n")
text_file.write("{one}: {two}% ({three})".format(one=candidateList[1], two=candidate1PerDes, three=candidate1Votes))
text_file.write("\n")
text_file.write("{one}: {two}% ({three})".format(one=candidateList[2], two=candidate2PerDes, three=candidate2Votes))
text_file.write("\n")
text_file.write("{one}: {two}% ({three})".format(one=candidateList[3], two=candidate3PerDes, three=candidate3Votes))
text_file.write("\n")
text_file.write("------------------------------")
text_file.write("\n")
text_file.write("Winner: {str}".format(str=winner))
text_file.write("\n")
text_file.write("------------------------------")
text_file.close()
