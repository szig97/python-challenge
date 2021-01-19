#1. Import the modules
import os 
import csv

#2. Set csv path
pypollcsv = os.path.join("Resources", "election_data.csv")

#3. Set initial variables
votes = []
county = []
candidates = []
khan = []
correy = []
li = []
otooley = []

#4. Open the csv
with open(pypollcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    #5. Count total votes
    total_votes = (len(votes))
    print(total_votes)

    #6. Count votes by person
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)
    print(khan_votes)
    print(correy_votes)
    print(li_votes)
    print(otooley_votes)

    #7. Calculate Percentages
    khan_percent = round(((khan_votes / total_votes) * 100), 2)
    correy_percent = round(((correy_votes / total_votes) * 100), 2)
    li_percent = round(((li_votes / total_votes) * 100), 2)
    otooley_percent = round(((otooley_votes / total_votes) *100), 2)
    print(khan_percent)
    print(correy_percent)
    print(li_percent)
    print(otooley_percent)

    #8. Determine the Winnner
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"
    elif li_percent > max(khan_percent, correy_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"

    #9. Print the results
    print(f"Election Results")
    print(f"----------------------------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"----------------------------------------------")
    print(f"Khan: {khan_percent}% ({khan_votes})")
    print(f"Correy: {correy_percent}% ({correy_votes})")
    print(f"Li: {li_percent}% ({li_votes})")
    print(f"O'Tooley: {otooley_percent}% ({otooley_votes})")
    print(f"----------------------------------------------")
    print(f"Winner: {winner}")

    #10. Export the data to a text file
    election_results = os.path.join("Analysis", "election_results.txt")
    with open(election_results, "w") as outfile:
        outfile.write(f"Election Results\n")
        outfile.write(f"----------------------------------------------\n")
        outfile.write(f"Total Votes: {total_votes}\n")
        outfile.write(f"Khan: {khan_percent}% ({khan_votes})\n")
        outfile.write(f"Correy: {correy_percent}% ({correy_votes})\n")
        outfile.write(f"Li: {li_percent}% ({li_votes})\n")
        outfile.write(f"O'Tooley: {otooley_percent}% ({otooley_votes})\n")
        outfile.write(f"----------------------------------------------\n")
        outfile.write(f"Winner: {winner}")