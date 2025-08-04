from InstagramFollowerBot import InstagramFollowerBot

chrome_driver_path = "/Users/bodemustafa/Development/chromedriver"

test = InstagramFollowerBot()
test.login()
test.find_followers()
test.follow()

