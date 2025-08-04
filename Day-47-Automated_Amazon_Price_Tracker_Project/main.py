import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os
from flask.cli import load_dotenv
import re

url = "https://www.amazon.com/InnoView-Portable-Ultra-Slim-Computer-Kickstand/dp/B0BJP8BNX6/ref=sr_1_12_sspa?crid=1YF40NRGHJIK9&dib=eyJ2IjoiMSJ9.K8ly-zQAs5p1oKIQQS-BmSqf3c8AljCYKhmEVz1mSyMmXSMoZGN4BgHhKyuK_khD0SelSaEld7k6yfM6G3x_Yt8XdHVRNYRu4U_HpV918xcJT4S4crl8meajxb3AtG2H6Flu2176aaDm7RP0y58Jro-OUTraZP3SNplLSTLrTcconI0-U8zh_-n98dHVI9EhXGLHwo9shgkUWaEB9XImNRPkWddNVyyhz8_dvxT6DgM.Wr8mz3UjOsxiXjNUKIqm6MEz3FKDyQdMscPjHnbSkCY&dib_tag=se&keywords=portable%2Bmonitor&qid=1738331348&sprefix=port%2Caps%2C204&sr=8-12-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&smid=A1WGRES5G20H4M&th=1"
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
          "Accept-Language":"en-US,en;q=0.9,ar;q=0.8,tr;q=0.7"}
response = requests.get(url,headers=header)

data =  response.text

soup = BeautifulSoup(data,"html.parser")
print(soup.prettify())

price  = soup.find(name="span",class_="aok-offscreen")
title = soup.find(name="span",class_="a-size-large product-title-word-break").getText()

just_num = float(price.getText().replace("$","").split()[0])

title_cleaned = re.sub(r'\s+', ' ', title.strip())

# print(title_cleaned)

link="https://appbrewery.github.io/instant_pot/"

load_dotenv()

password = os.getenv("password")
my_email = os.getenv("my_email")

if just_num<170:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="abdutries@gmail.com",
                            msg=f"Subject:Amazon Price Alert!!\n\n {title_cleaned} is now for ${just_num}\n {link}".encode("utf-8"))
