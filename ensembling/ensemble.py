import pandas as pd
import glob, os

sub_dir = './submissions/' 

submission_files = glob.glob(sub_dir+"5*/*.csv")
print(submission_files) 

sub_files = [pd.read_csv(file_path) for file_path in submission_files]

submissions = [sub_file['breed'] for sub_file in sub_files]

print(submissions[0,:])

# from collections import Counter 
  
# def most_frequent(List): 
#     occurence_count = Counter(List) 
#     return occurence_count.most_common(1)[0][0] 
    
# List = [2, 1, 2, 2, 1, 3] 
# print(most_frequent(List)) 

