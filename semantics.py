# python script to analyze semantics of text
# this text will be entered by the user in the journal entry and will be analyzed
# to gather semantics on the journal entry

# import packages
import nltk
import nrclex
from nrclex import NRCLex

def main():
    

# to gather semantic data
def getSemantics(text):
    data = NRCLex(text)
    top_emotions = data.top_emotions

    emotions_without_score = []
    # get only the emotions without the value score
    for emotion,i in enumerate(top_emotions):
        if i == 3:
            return emotions_without_score
        
        # append the next emotion
        emotions_without_score.append(top_emotions[i][0])


# to control the main method execution
if __name__ == '__name__':
    main()