import time
from InternetSpeedTwitterBot import InternetSpeedTwitterBot


Promised_DOWN = 30
Promised_UP = 5
chrome_driver_path = "/Users/bodemustafa/Development/chromedriver"
Twitter_Username = "your email"
Twitter_Password = "your password"


gaga = InternetSpeedTwitterBot()
gaga.get_internet_speed()
time.sleep(4)
gaga.tweet_at_provider(Twitter_Username,Twitter_Password)
