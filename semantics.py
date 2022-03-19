# python script to analyze semantics of text
# this text will be entered by the user in the journal entry and will be analyzed
# to gather semantics on the journal entry

# import packages
import sys
import pandas
from nrclex import NRCLex

# does all the work
def getSemantics(text):
    data = NRCLex(text)
    top_emotions = data.top_emotions

    # get only the emotions without the value score and return the top 3 emotions
    emotions_wo_score = [emotion[0] for emotion in top_emotions]
    #return emotions_wo_score

    if len(emotions_wo_score) > 3:
        return emotions_wo_score[0:3]
    else:
        return emotions_wo_score

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for arg in sys.argv:
        print(getSemantics(arg))