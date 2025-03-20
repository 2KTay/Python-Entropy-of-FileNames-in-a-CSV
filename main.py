'''
Python Entropy of FileNames in a CSV

to look through CSV, extract the filepaths, calculate the entropy score
using Shannon entropy, display top 10 and bottom 10

change filename on line 56 if necessary

this works for and for run once
Run Keys:Type,Run Keys:Name,Run Keys:Command Line, Count
with 5 lines csv


but has a issue with bigfile.csv with 100 lines as it is not calcuating properly


Author: Taemoor Hasan
'''

#Search up standard math library for entropy python

import pandas as pd
import re
import matplotlib.pyplot as plt


# Shannon entropy function
import math
from collections import Counter


#entropy of bigrams
#try other algoritms

#def shannon_entropy(s :str)
def shannon_entropy(s):

    freq = Counter(s)
    length = len(s)

    #length might be playing a huge factor in this then it supposed to
    #math.log on length?
    entropy = -sum((count / length) * math.log2(count / length) for count in freq.values())

    # avoid math domain error for one unique character
    num_unique = len(freq)
    if num_unique > 1:
        entropy /= math.log2(num_unique)

    return entropy


# Function to extract exe name or  file path
def extract_exe(command_line):

    # Use regex to find the .exe file in the command line
    #matehches everything after the last slash that ends with .exe
    #+).exe
    #use the dollar sign at the end
    #(),exe,pipe,ps1,cmd, extensions
    #learn regex 101

    #NOTE: some programs do not end with .exe
    match = re.search(r'\\([^\\]+\.exe)', command_line)
    if match:
        return match.group(0)
    return ""



#change file name if necessary
df = pd.read_csv('logs.csv')


#User input for filename (if needed)
'''
file_Name_log=input("What is the filename?\n")

if '.csv' in file_Name_log:
    df = pd.read_csv(file_Name_log)
else:
    df = pd.read_csv(file_Name_log+'.csv')
    '''


#to extract the .exe filename or path
if 'Run Keys:Command Line' in df.columns:
    df['Executable Path'] = df['Run Keys:Command Line'].apply(extract_exe)
elif 'Run Once Keys:Command Line' in df.columns:
    df['Executable Path'] = df['Run Once Keys:Command Line'].apply(extract_exe)

# calculate entropy extracted executable path
df['Entropy'] = df['Executable Path'].apply(shannon_entropy)



df_sorted_big = df.sort_values(by='Entropy', ascending=False)
df_sorted_small = df.sort_values(by='Entropy', ascending=True)

#top 10 entries based on entropy (highest entropy)
top_10 = df_sorted_big.head(10)

# bottom 10 entries based on entropy (lowest entropy)
bottom_10 = df_sorted_small.head(10)



nameRunKeys= 'Run Keys:Name' if 'Run Keys:Name' in df.columns else 'Run Once Keys:Name'

# Show the top 10 entries with the name, path, and entropy
print("Top 10 Entries Based on Entropy:")
print(top_10[[nameRunKeys, 'Executable Path', 'Entropy']])

print("\nBottom 10 Entries Based on Entropy:")
print(bottom_10[[nameRunKeys, 'Executable Path', 'Entropy']])



# Plotting the top 10 entries
plt.figure(figsize=(10, 6))
plt.barh(top_10[nameRunKeys], top_10['Entropy'], color='green')
plt.xlabel('Entropy')
plt.ylabel('Executable Name')
plt.title('Top 10 Entries Based on Entropy')
plt.gca().invert_yaxis()  # Invert the y-axis to display the highest entropy at the top
plt.show()

# Plotting the bottom 10 entries
plt.figure(figsize=(10, 6))
plt.barh(bottom_10[nameRunKeys], bottom_10['Entropy'], color='red')
plt.xlabel('Entropy')
plt.ylabel('Executable Name')
plt.title('Bottom 10 Entries Based on Entropy')
plt.gca().invert_yaxis()  # Invert the y-axis to display the highest entropy at the top
plt.show()