#modules
import os
import csv

# The total number of votes cast
total_votes= 0
# A complete list of candidates who received votes
candidates_vote = {}
candidates_options = []
# The percentage of votes each candidate won
percentage_votes ={}
# The total number of votes each candidate won
candidates_total = 0
# The winner of the election based on popular vote
popular_vote ={}
winning_count = 0
winning_candidate = ""

csvpath = os.path.join("Resources","election_data.csv")
out_path = os.path.join("analysis", "election_analysis.txt")
#open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #read the header row
    header_row =next(csvreader)

    # Loop each row in the CSV file.
    for row in csvreader:
    # Add to the total vote count.
        total_votes = total_votes + 1
    # Get the candidate name from each row.
        candidate_name = row[2]
        if candidate_name not in candidates_options:
            candidates_options.append(candidate_name)
            candidates_vote[candidate_name] = 0
        candidates_vote[candidate_name]+= 1
        
with open(out_path,"w") as txt_file:
    text_out = (
        f"Election Results \n"
        f"-------------------------\n"
        f"Total Votes:{total_votes} \n"
        f"-------------------------\n")
    print(text_out)

    txt_file.write(text_out)

    for candidate in candidates_vote:
        votes = candidates_vote.get(candidate)

        percentage_votes = votes/total_votes * 100
        candidate_results = (f"{candidate}: {percentage_votes}% ({votes:,})\n")
        print(candidate_results)

        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate


    #Print Candidate voter count and percentage
        txt_file.write(candidate_results)

        winning_candidate_txt = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"-------------------------"
            )
    print(winning_candidate_txt)   
    txt_file.write(winning_candidate_txt)