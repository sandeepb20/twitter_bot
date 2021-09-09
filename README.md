# Script to post multiple status on twitter (i.e. TWITTER STORM)
This program can post upto maximum limit of twitter(around 300 tweets) within seconds.
### Pre-requisites
1. Write the main body of your tweet in `body.txt` file.
2. Mentions all tags in  `tags.txt` file.
3. Mentions all hashtags in `hashtags.txt` file.
### Instructions to run locally:
1. Run `pip freeze > requirements.txt` dependencies.
2. Give command `python3 main.py` to run the program

### Working
Program randomly select 3 different lines of body, any 3 tags and 3 hashtags to create a tweet post. After authenticating your keys this will post `n` tweets on your account's feed.<br>
Here `n` is taken as user input.
### Sample Output
...
