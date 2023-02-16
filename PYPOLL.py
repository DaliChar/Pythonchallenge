

# In[1]:


#directing python to our intended file 
import os
import csv


# In[2]:


#making declarations 
votes_cast = 0
candidates = []
unique_candidate_votes = []


# Reads in the CSVs for both PyPoll using Python
# 
# Successfully stores the header row 

# In[3]:


csvpath = os.path.join('election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None) 

    for row in csvreader:
        votes_cast += 1
        if votes_cast == 1:
            candidates.append(row[2])
            unique_candidate_votes.append(1)
        else:
            try:
                candidate_one = candidates.index(row[2])
                unique_candidate_votes[candidate_one] += 1
            except:
                candidates.append(row[2])
                unique_candidate_votes.append(1)


# In[4]:


#attempting to list candidate names 
candidate_list =[]
unique_candidate=[]

candidate_list.append(row[2])
for candidate in set(candidates):
   unique_candidate.append(candidate)
   
   names = candidate_list.count(candidate)


# In[ ]:


winner = candidates[0]
results = []
maxvotes = unique_candidate_votes[0]
for i in range(len(candidates)):
    if unique_candidate_votes[i] > maxvotes:
        winner = candidates[i]
        highest_votes = unique_candidate_votes[i]
    percent = 100 * unique_candidate_votes[i] / votes_cast
    results.append(f"{candidates[i]}: {round(percent,3)} % ({unique_candidate_votes[i]})")



results.append("Election Results\n-------------------------")
results.append(f"Total Votes: {votes_cast}\n-------------------------")
results.append(f"-------------------------\nWinner: {winner}\n-------------------------")


# In[ ]:


filename = 'Election Results.txt'
with open(filename, 'w') as file:
    for result in results:
        print(result)
        file.write(result + '\n')

