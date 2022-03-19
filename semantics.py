# python script to analyze semantics of text
# this text will be entered by the user in the journal entry and will be analyzed
# to gather semantics on the journal entry

# import packages
import sys
import pandas as pd
from nrclex import NRCLex

# called when script is called
def main():
    print(getSemantics(sys.argv[1]))

# to gather semantic data
def getSemantics(text):
    data = NRCLex(text)
    top_emotions = data.top_emotions

    emotions_wo_score = []
    # get only the emotions without the value score
    for emotion,i in enumerate(top_emotions):
        if i == 3:
            return emotions_wo_score
        
        # append the next emotion
        emotions_wo_score.append(top_emotions[i][0])