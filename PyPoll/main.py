import os
import csv
election_data = '/Users/macowner/Desktop/03-Python/Instructions/PyPoll/Resources/election_data.csv'
total_number = 0
candidates = []
Khan_vote = 0
Correy_vote = 0
Li_vote = 0
Tooley_vote = 0



with open(election_data, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    for row in csvreader:    
        #print(row)   
        #break
        total_number = total_number + 1
        if row[2] not in candidates:
            candidates.append(row[2])
            
        if row[2] == "Khan":
            Khan_vote = Khan_vote + 1
        elif row[2] == "Correy":
            Correy_vote = Correy_vote + 1
        elif row[2] == "Li":
            Li_vote = Li_vote + 1
        elif row[2] == "O'Tooley":
            Tooley_vote = Tooley_vote + 1
    
        
percentage_Khan = round(Khan_vote/total_number,3)*100
percentage_Correy = round(Correy_vote/total_number,3)*100
percentage_Li = round(Li_vote/total_number,3)*100
percentage_Tooley = round(Tooley_vote/total_number,3)*100
list = (float(percentage_Khan),float(percentage_Correy),float(percentage_Li),float(percentage_Tooley))
if max(list) == list[0]:
    winner = "Khan"
elif max(list) == list[1]:
    winner = "Correy"
elif max(list) == list[2]:
    winner = "Li"
elif max(list) == list[3]:
    winner = "O'Tooley"


output = (
     "Election Results\n"
     "----------------------------\n"
     f"Total Votes: {total_number}\n"
     "----------------------------\n"
     f"Khan:   {percentage_Khan:.3f}%  ({Khan_vote})\n"
     f"Correy: {percentage_Correy:.3f}% ({Correy_vote})\n"
     f"Li: {percentage_Li:3f}% ({Li_vote})\n"
     f"O'Tooley: {percentage_Tooley:3f}% ({Tooley_vote})\n"
     "----------------------------\n"   
     f"Winner: {winner}\n"
     "----------------------------")
   

# Print the output (to terminal)
print(output)
output_file = os.path.join('new_file.txt')
# Export the results to text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)
