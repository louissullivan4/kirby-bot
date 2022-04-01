from json.tool import main
import requests
import json
import re

from keys import *

bearer_token = bearer_token()

def bearer_oauth(r):
	r.headers["Authorization"] = f"Bearer {bearer_token}"
	r.headers["User-Agent"] = "v2RecentSearchPython"
	return r

def connect_to_endpoint(url, params):
	response = requests.get(url, auth=bearer_oauth, params=params)
	return response.json()

def remove_emoji(string):
	emoji_pattern = re.compile("["
	u"\U0001F600-\U0001F64F" u"\U0001F680-\U0001F6FF" u"\U0001F1E0-\U0001F1FF" u"\U00002500-\U00002BEF"
	u"\U00002702-\U000027B0"u"\U00002702-\U000027B0"u"\U000024C2-\U0001F251"u"\U0001f926-\U0001f937"
	u"\U00010000-\U0010ffff"u"\u2640-\u2642"u"\u2600-\u2B55"u"\u200d"u"\u23cf"u"\u23e9"u"\u231a"
	u"\ufe0f"u"\u3030""]+", flags=re.UNICODE)
	return emoji_pattern.sub(r'', string)

def filter_tweet(tweet):
	newline_remove = tweet.replace("\n", " ")
	rt_remove = re.compile('RT @').sub('@', newline_remove, count=1)
	username_remove = re.sub('@[^\s]+', '', rt_remove)
	filtered = username_remove.strip()
	string_encode = filtered.encode("ascii", "ignore")
	string_decode = string_encode.decode()
	string_decode = " ".join(string_decode.split())
	return string_decode

def twitter_search():
    acc_id = str(user_account)
    twitter_dict = {}
    query_params = {}
    search_url = 'https://api.twitter.com/2/users/%s/tweets?exclude=replies,retweets'%acc_id
    dict_response = connect_to_endpoint(search_url, query_params)
    dict_response = dict(dict_response)
    i = 0
    while i < len(dict_response['data']):
        tweet = dict_response['data'][i]["text"]
        no_emoji = remove_emoji(tweet)
        filtered_tweet = filter_tweet(no_emoji)
        twitter_dict[i] = filtered_tweet
        i += 1
    return twitter_dict

# print(twitter_search())