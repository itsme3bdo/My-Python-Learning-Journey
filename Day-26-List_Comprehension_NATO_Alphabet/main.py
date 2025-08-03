# # student_dict = {
# #     "student": ["Angela", "James", "Lily"],
# #     "score": [56, 76, 98]
# # }
# #
# # #Looping through dictionaries:
# # for (key, value) in student_dict.items():
# #     #Access key and value
# #     pass
# #
# import pandas as pd
# # student_data_frame = pandas.DataFrame(student_dict)
# #
# # #Loop through rows of a data frame
# # for (index, row) in student_data_frame.iterrows():
# #     #Access index and row
# #     #Access row.student or row.score
# #     pass
# #
# # # Keyword Method with iterrows()
# # # {new_key:new_value for (index, row) in df.iterrows()}
#
# #TODO 1. Create a dictionary in this format:
# nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
# diccc = {row.letter:row.code for (index,row) in nato_alphabet.iterrows()}
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# answer = list(input("Enter a word:").upper())
# final = [value for key,value in diccc.items() if key in answer]
# print(final)

import pandas as pd

nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
diccc = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
print(nato_alphabet)
def gen_phonetic():
    answer = input("Enter a word:").upper()
    try:
        final = [diccc[let] for let in answer]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        gen_phonetic()
    else:
        print(final)

gen_phonetic()


