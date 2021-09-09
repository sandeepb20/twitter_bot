import tweepy
import random

def auth_keys():
    twitter_auth_keys = {
    "api_key"             : "REPLACE THIS WITH YOUR ***API key***",
    "api_secret"          : "REPLACE THIS WITH YOUR ***API key secret***",
    "access_token"        : "REPLACE THIS WITH YOUR ***access token***",
    "access_token_secret" : "REPLACE THIS WITH YOUR ***access token secret*** "
    }
    return twitter_auth_keys


def random_line(file_name):
    lines = open(file_name).read().splitlines()
    return random.choice(lines)

def create_tweet():
    body1 = random_line('body.txt')
    body2 = random_line('body.txt')
    while(body1 == body2):
        body2 = random_line('body.txt')
    body3 = random_line('body.txt')
    while(body3 == body2 or body1 == body3):
        body3 = random_line('body.txt')

    tag1 = random_line('tags.txt')
    tag2 = random_line('tags.txt')
    while(tag1 == tag2):
        tag2 = random_line('tags.txt')
    tag3 = random_line('tags.txt')
    while(tag3 == tag2 or tag1 == tag3):
        tag3 = random_line('tags.txt')
        
    hashtag1 = random_line('hashtags.txt')
    hashtag2 = random_line('hashtags.txt')
    while(hashtag1 == hashtag2):
        hashtag2 = random_line('hashtags.txt')
    hashtag3 = random_line('hashtags.txt')
    while(hashtag3 == hashtag2 or hashtag1 == hashtag3):
        hashtag3 = random_line('hashtags.txt')
    
    final_msg = body1 +" "+ body2 +" "+ body3+ "\n" + tag1+ " \n"+ tag2 + " \n"+ tag3 + " \n" + hashtag1 +" \n"+ hashtag2 +" \n"+hashtag3 +" \n"
    return final_msg

def main():
    twitter_auth_keys = auth_keys()
 
    auth = tweepy.OAuthHandler(
            twitter_auth_keys['api_key'],
            twitter_auth_keys['api_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    n = int(input("Enter No of iterations:"))
    for i in range(n):
        tweet =  "Tweet Number : "+ str(i) +"\n" +create_tweet()
        #print(tweet)
        status = api.update_status(status=tweet)
 
if __name__ == "__main__":
    main()
