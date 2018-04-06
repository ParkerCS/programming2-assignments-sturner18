# PROBLEM 1 (12pts)
# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect the twitter feed in Chrome.
# You'll notice that the tweets are stored in a ordered list <ol></ol>, and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and requests to grab the text contents of last 5 tweetslocated on the twitter page you chose.
# Print the tweets in a nicely formatted way.
# Have fun.  Again, nothing explicit.
from bs4 import BeautifulSoup
import requests

url = "https://twitter.com/barackobama?lang=en"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")
# print(soup.prettify())

tweets = soup.findAll("p", class_="tweet-text")
# print(tweets)
# for tweet in tweets:
    # print("\n")
    # print(tweet.text)

for i in range(5):
    print("\n")
    print(tweets[i].text.strip())

# (20pts)
# Below is a link to a 10-day weather forecast at weather.com
# Use urllib and BeautifulSoup to scrape data from the weather table.
# Print a synopsis of the weather for the next 10 days.
# Include the day and date, description, high and low temp, chance of rain, and wind. (2pts each)
# Print the weather for each of the next 10 days to the user in a readable sentences.
# You can customize the text as you like, but it should be readable as a sentence without errors. (10pts)
# You will need to target specific classes or other attributes to pull some parts of the data.
# Sample sentence:  
# Wednesday, April 4 will be Partly Cloudy/Windy with a High of 37 degrees and a low of 25, humidity at 52%.  There is 0% chance of rain with winds out of the WNW at 22 mph.

url = "https://weather.com/weather/tenday/l/Chicago+IL+USIL0225:1:US"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

days_list = []
days = soup.findAll(class_="date-time")
for day in days:
    days_list.append(day.text.strip())

dates_list = []
dates = soup.findAll(class_="day-detail")
for date in dates:
    dates_list.append(date.text.strip())

descriptions_list = []
descriptions = soup.findAll(class_="description")
for description in descriptions:
    descriptions_list.append(description.text.strip())

descriptions_list = descriptions_list[1:]

temps_list = []
temps = soup.findAll(class_="temp")
for temp in temps:
    temps_list.append(temp.text.strip())

temps_list = temps_list[1:]

percips_list = []
precips = soup.findAll(class_="precip")
for precip in precips:
    percips_list.append(precip.text.strip())

percips_list = percips_list[1:]

winds_list = []
winds = soup.findAll(class_="wind")
for wind in winds:
    winds_list.append(wind.text.strip())

winds_list = winds_list[1:]

humidity_list = []
humidity = soup.findAll(class_="humidity")
for hum in humidity:
    humidity_list.append(hum.text.strip())

humidity_list = humidity_list[1:]

for i in range(len(days_list)):
    print("\n", days_list[i] + ",", dates_list[i],  "will be", descriptions_list[i], "with", percips_list[i], "chance of precipitation" + ".", "The wind will be traveling", winds_list[i], "with a", humidity_list[i], "humidity and a high/low temperature of", temps_list[i] + ".", "\n")