# You hv been two lists, one containing the names of the students and the other containing 
# their corresponding scores in test
# Create a dictionary where the keys are the students names and the values are their scores.
# Then find and print the average score.
# you are only allowed to use - LEN() function.

lst1=['Rohan', 'Mohan', 'Shivam', 'Aman']
list=[80, 86, 90, 94]
dic={}
score = 0
total_score=0

for i in range(len(lst1)):
    dic[lst1[i]]=list[i]

print(dic)

for key in list:
    total_score += key
    # score += 1

average_score=total_score/len(list)#score

print(f"The average score is: {average_score}")