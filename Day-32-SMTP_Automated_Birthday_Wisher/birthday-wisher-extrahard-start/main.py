import smtplib
import datetime as dt
from random import choice
import pandas as pd

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
with open("./letter_templates/letter_1.txt","r") as l1:
    letter1 = l1.read()
with open("./letter_templates/letter_2.txt", "r") as l2:
    letter2 = l2.read()
with open("./letter_templates/letter_3.txt", "r") as l3:
    letter3 = l3.read()

data = pd.read_csv("birthdays.csv")
info = {row["name"]: {"email": row.email,"year":row.year,"month":row.month,"day":row.day}for (_,row) in data.iterrows()}
print(info)
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = now.day
monthy = now.month

for x in info.keys():
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    chosen_letter = choice([letter1, letter2, letter3])
    new_letter = chosen_letter.replace("[NAME]", f"{x}")
    # 4. Send the letter generated in step 3 to that person's email address.

    if today==info[x]["day"] and monthy==info[x]["month"]:
        print(new_letter)
        password = "ltuo xjld loec qzvd"
        my_email = "bodeman2000@gmail.com"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=info[x]["email"],
                                msg=f"Subject:Happy Birthday!!\n\n{new_letter}")







