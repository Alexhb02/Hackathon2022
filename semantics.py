# python script to analyze semantics of text
# this text will be entered by the user in the journal entry and will be analyzed
# to gather semantics on the journal entry

# import packages
import sys
import pandas as pd
from nrclex import NRCLex
import random

# store a set of suggestions based on the ten emotions from NRCLex
suggestion_dict = {'fear' : ['If you start to get a faster heartbeat or sweating palms, the best thing is not to fight it. Stay where you are and simply feel the panic without trying to distract yourself. Place the palm of your hand on your stomach and breathe slowly and deeply. The goal is to help the mind get used to coping with panic, which takes the fear of fear away.',
                             'Avoiding fears only makes them scarier. Whatever your fear, if you face it, it should start to fade. If you panic one day getting into an elevator, for example, it is best to get back into a lift the next day.',
                             'It is impossible to think clearly when you are flooded with fear or anxiety. The first thing to do is take time out so you can physically calm down. Distract yourself from the worry for 15 minutes by walking around the block, making a cup of tea or having a bath.',
                             'Try imagining the worst thing that can happen – perhaps it is panicking and having a heart attack. Then try to think yourself into having a heart attack. It is just not possible. The fear will run away the more you chase it.',
                             'It sometimes helps to challenge fearful thoughts. For example, if you are scared of getting trapped in an elevator and suffocating, ask yourself if you have ever heard of this happening to someone. Ask yourself what you would say to a friend who had a similar fear.',
                             'Life is full of stresses, yet many of us feel that our lives must be perfect. Bad days and setbacks will always happen, and it is important to remember that life is messy.',
                             'Take a moment to close your eyes and imagine a place of safety and calm. It could be a picture of you walking on a beautiful beach, or snuggled up in bed with the cat next to you, or a happy memory from childhood. Let the positive feelings soothe you until you feel more relaxed.',
                             'Sharing fears takes away a lot of their scariness. If you cannot talk to a partner, friend or family member, call a helpline such as Breathing Space.',
                             'Lots of people turn to alcohol or drugs to self-treat anxiety, but this will only make matters worse. Simple, everyday things like a good nights sleep, a wholesome meal, and a walk are often the best cures for anxiety.',
                             'Give yourself a treat. When you have made that call you have been dreading, for example, reinforce your success by treating yourself to a massage, a country walk, a meal out, a book, a DVD, or whatever little gift makes you happy.'],
                   'anger' : ['In the heat of the moment, it is easy to say something you will later regret. Take a few moments to collect your thoughts before saying anything — and allow others involved in the situation to do the same.',
                              'As soon as you are thinking clearly, express your frustration in an assertive but nonconfrontational way. State your concerns and needs clearly and directly, without hurting others or trying to control them.',
                              'Physical activity can help reduce stress that can cause you to become angry. If you feel your anger escalating, go for a brisk walk or run, or spend some time doing other enjoyable physical activities.',
                              'Timeouts are not just for kids. Give yourself short breaks during times of the day that tend to be stressful. A few moments of quiet time might help you feel better prepared to handle what is ahead without getting irritated or angry.',
                              'Instead of focusing on what made you mad, work on resolving the issue at hand. Does your childs messy room drive you crazy? Close the door. Is your partner late for dinner every night? Schedule meals later in the evening — or agree to eat on your own a few times a week. Remind yourself that anger will not fix anything and might only make it worse.',
                              'To avoid criticizing or placing blame — which might only increase tension — use "I" statements to describe the problem. Be respectful and specific. For example, say, "I am upset that you left the table without offering to help with the dishes" instead of "You never do any housework."',
                              'Forgiveness is a powerful tool. If you allow anger and other negative feelings to crowd out positive feelings, you might find yourself swallowed up by your own bitterness or sense of injustice. But if you can forgive someone who angered you, you might both learn from the situation and strengthen your relationship.',
                              'Lightening up can help diffuse tension. Use humor to help you face what is making you angry and, possibly, any unrealistic expectations you have for how things should go. Avoid sarcasm, though — it can hurt feelings and make things worse.',
                              'When your temper flares, put relaxation skills to work. Practice deep-breathing exercises, imagine a relaxing scene, or repeat a calming word or phrase, such as "Take it easy." You might also listen to music, write in a journal or do a few yoga poses — whatever it takes to encourage relaxation.',
                              'Learning to control anger is a challenge for everyone at times. Seek help for anger issues if your anger seems out of control, causes you to do things you regret or hurts those around you.'],
                   'anticipation' : [],
                   'trust' : [],
                   'surprise' : [],
                   'positive' : [],
                   'negative' : [],
                   'sadness' : [],
                   'disgust' : [],
                   'joy' : []}

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

# to give suggestions
def giveSuggestions(emotions):
    # create a suggestion list to give to the user
    suggestions = []
    for e in emotions:
        # generate index of suggestion to give
        index = random.randint(0,9)
        suggestions.append(suggestion_dict[e][index])

    return suggestions

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        emotions = getSemantics(arg)
        suggestions = giveSuggestions(emotions)
        print(suggestions)