Final Project submission - Bunci Patel 

I used an API to web scrape a site using advanced Python scripting 

Why? - I want a script where I can input any topic or product and it will output a ratio of how well it's represented on the internet, if it's positive, then chances are the product is good or the topic is positive. 

How I implemented it: Reddit API, Python, PRAW 

Prereqs: 
Install PRAW - open powershell as admin on a computer with Python3 installed. type 'pip install praw' 
Create a reddit account at reddit.com and create a free app (https://www.reddit.com/prefs/apps) for personal use and scripting, choose whatever name and set the redirect URL to https://google.com/
Open the script in Python IDLE 
Copy the Client ID that's under the "personal use script" banner and copy it into the script, keep the single quotes 
Copy the secret key into the script that says client secret 

Save and run the script 

Input a one word topic or brand or product then press enter (WARNING: Reddit is uncensored, you will see profanity based on what you're searching for) 

Note: Multi words are allowed but results may not be accurate. 

For exmaple, as of 4/20/23, I got this result when searching for SpaceX:

Output: 
*tons of reviews, both positive and negative, see https://i.imgur.com/5sfghED.png*
Take this ratio with a grain of salt. Out of 231 comments, 95.24% are positive and 4.76% are negative.

Notes: The user has the options to scroll back up and review a summary of the top 5 reddit posts that are related to your topic. 
