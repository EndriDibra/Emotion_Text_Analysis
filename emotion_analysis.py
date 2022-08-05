# Author: Endri Dibra
# Calling the required libraries
from textblob import TextBlob as tb


# The function below, takes text and analyzes
# it if it is negative or positive or neutral
# then displays the right answer
def sentiment_analysis(text):

    if text.sentiment.polarity < 0:

        print("Your thoughts are negative")
        print(text.sentiment)

    elif text.sentiment.polarity > 0:

        print("Your thoughts are positive")
        print(text.sentiment)

    else:

        print("Your thoughts are neutral")
        print(text.sentiment)

# input from user to check the program
print("Please enter your text")
text = tb(input())

# calling the function
sentiment_analysis(text)
