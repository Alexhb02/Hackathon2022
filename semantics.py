# python script to analyze semantics of text
# this text will be entered by the user in the journal entry and will be analyzed
# to gather semantics on the journal entry

# import packages
import sys
import pandas as pd
from nrclex import NRCLex

# to gather semantic data
def getSemantics(text):
    data = NRCLex(text)
    top_emotions = data.top_emotions

    # get only the emotions without the value score
    emotions_wo_score = [emotion[0] for emotion in top_emotions]
    if len(emotions_wo_score) > 3:
        return emotions_wo_score[0:3]
    else:
        return emotions_wo_score

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        print(getSemantics(arg))