#TODO: Create a letter using starting_letter.txt
with open("Input/Letters/starting_letter.txt", mode = "r") as file:
    letter = file.read()
print(letter)
names_list=[]
#for each name in invited_names.txt
with open("Input/Names/invited_names.txt",mode = "r") as namez:
    for x in namez:
        names_list.append(x)
print(names_list)
#Replace the [name] placeholder with the actual name.
for x in names_list:
    new_name = x.replace("\n","")
    replaced = letter.replace("[name]",new_name)

# #Save the letters in the folder "ReadyToSend".
#     with open(f"Output/ReadyToSend/letter_for_{new_name}","w") as new:
#         new.write(replaced)
    print(replaced)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp