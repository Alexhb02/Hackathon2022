# python script to analyze semantics of text
# this text will be entered by the user in the journal entry and will be analyzed
# to gather semantics on the journal entry

# import packages
import sys
from nrclex import NRCLex
import random

# store a set of suggestions based on the ten emotions from NRCLex
suggestion_dict = {'fear': [
                        'If you start to get a faster heartbeat or sweating palms, the best thing is not to fight it. Stay where you are and simply feel the panic without trying to distract yourself. Place the palm of your hand on your stomach and breathe slowly and deeply. The goal is to help the mind get used to coping with panic, which takes the fear of fear away.',
                        'Avoiding fears only makes them scarier. Whatever your fear, if you face it, it should start to fade. If you panic one day getting into an elevator, for example, it is best to get back into a lift the next day.',
                        'It is impossible to think clearly when you are flooded with fear or anxiety. The first thing to do is take time out so you can physically calm down. Distract yourself from the worry for 15 minutes by walking around the block, making a cup of tea or having a bath.',
                        'Try imagining the worst thing that can happen, perhaps it is panicking and having a heart attack. Then try to think yourself into having a heart attack. It is just not possible. The fear will run away the more you chase it.',
                        'It sometimes helps to challenge fearful thoughts. For example, if you are scared of getting trapped in an elevator and suffocating, ask yourself if you have ever heard of this happening to someone. Ask yourself what you would say to a friend who had a similar fear.',
                        'Life is full of stresses, yet many of us feel that our lives must be perfect. Bad days and setbacks will always happen, and it is important to remember that life is messy.',
                        'Take a moment to close your eyes and imagine a place of safety and calm. It could be a picture of you walking on a beautiful beach, or snuggled up in bed with the cat next to you, or a happy memory from childhood. Let the positive feelings soothe you until you feel more relaxed.',
                        'Sharing fears takes away a lot of their scariness. If you cannot talk to a partner, friend or family member, call a helpline such as Breathing Space.',
                        'Lots of people turn to alcohol or drugs to self-treat anxiety, but this will only make matters worse. Simple, everyday things like a good nights sleep, a wholesome meal, and a walk are often the best cures for anxiety.',
                        'Give yourself a treat. When you have made that call you have been dreading, for example, reinforce your success by treating yourself to a massage, a country walk, a meal out, a book, a DVD, or whatever little gift makes you happy.'],
                   'anger': [
                       'In the heat of the moment, it is easy to say something you will later regret. Take a few moments to collect your thoughts before saying anything and allow others involved in the situation to do the same.',
                       'As soon as you are thinking clearly, express your frustration in an assertive but nonconfrontational way. State your concerns and needs clearly and directly, without hurting others or trying to control them.',
                       'Physical activity can help reduce stress that can cause you to become angry. If you feel your anger escalating, go for a brisk walk or run, or spend some time doing other enjoyable physical activities.',
                       'Timeouts are not just for kids. Give yourself short breaks during times of the day that tend to be stressful. A few moments of quiet time might help you feel better prepared to handle what is ahead without getting irritated or angry.',
                       'Instead of focusing on what made you mad, work on resolving the issue at hand. Does your childs messy room drive you crazy? Close the door. Is your partner late for dinner every night? Schedule meals later in the evening or agree to eat on your own a few times a week. Remind yourself that anger will not fix anything and might only make it worse.',
                       'To avoid criticizing or placing blame, which might only increase tension, use "I" statements to describe the problem. Be respectful and specific. For example, say, "I am upset that you left the table without offering to help with the dishes" instead of "You never do any housework."',
                       'Forgiveness is a powerful tool. If you allow anger and other negative feelings to crowd out positive feelings, you might find yourself swallowed up by your own bitterness or sense of injustice. But if you can forgive someone who angered you, you might both learn from the situation and strengthen your relationship.',
                       'Lightening up can help diffuse tension. Use humor to help you face what is making you angry and, possibly, any unrealistic expectations you have for how things should go. Avoid sarcasm, though, it can hurt feelings and make things worse.',
                       'When your temper flares, put relaxation skills to work. Practice deep breathing exercises, imagine a relaxing scene, or repeat a calming word or phrase, such as "Take it easy." You might also listen to music, write in a journal or do a few yoga poses, whatever it takes to encourage relaxation.',
                       'Learning to control anger is a challenge for everyone at times. Seek help for anger issues if your anger seems out of control, causes you to do things you regret or hurts those around you.'],
                   'anticipation': [
                       'Keep your head held high if things do not go your way. Know that in the end your feelings of anticipation are natural feelings towards the unknown. Try to come up with a plan for if things go the way you want or if things go another way.'],
                   'trust': [
                       'It is great that you feel trusting today! This is truly a hard state to attain because, as humans we naturally are taught not trust others. Take some time to do something nice for a stranger today!'],
                   'surprise': [
                       'Recognize how you cope with surprise - do you enjoy it? become stress? panic? Often times, surprise is a part of everyday life - recognizing this can make dealing with surprise easier.',
                       'The key to everything is your attitude. A positive attitude is an asset in unexpected situations. Not all unexpected events are negative. Sometimes, what seems like a problem, or even a disaster, could be a blessing in disguise. A negative event can awaken ambition, motivation, and persistence, which would lead to progress and success.',
                       'When making a plan, always have an alternate plan, in case the first plans fail. This would prevent you from falling into a state of helplessness, fear, and not knowing what to do next.',
                       'Wait for a few moments, before blurting out when confronting unexpected or unpleasant turns of fate. Before getting angry or panicking, look at what happened and assimilate the news. In many cases, this might something of minor importance that is easy to cope with. Maybe what happened is temporary, or something that can be easily fixed.',
                       'If what happened is irreversible, what good would you gain by becoming angry, stressed or panicked? You would gain nothing. Instead of getting flustered and confused, angry or feeling helpless, it would be much more useful to think constructively where you are going from there. You need to think how to adjust to the new situation and either fix it, improve it, or make the most of it.',
                       'Take the initiative, and introduce small changes into your life. Sometimes, in small and not important matters do things differently, without premeditating about them. This will help you cope more easily with surprises and events that are out of your control. In this way, you teach yourself to accept change.',
                       'Always focus on the present moment, living it the best, learning from it the most you can, and taking advantages of new opportunities that come your way. All there is, is the present moment, therefore, make the most of it, instead of thinking about what you lost, thinking about the past, or dwelling on how bad the situation is. This approach is useless and is a waste of time.',
                       'Learn and practice meditation. Even just 10 minutes of meditation every day can make a great change in your life, making you feel, calm, relaxed, and unperturbed by the events in your life. A certain amount of inner peace is most welcome in every situation, and meditation is one of the foremost ways leading to inner peace.'],
                   'positive': [
                       'The positivity flowing through you is awesome! Use that positivity to make headway on your goals and tackle those projects.'],
                   'negative': [
                       'Often times, when we feel things are not going our way, we tend to go over them multiple times. Be careful not to blow things out of proportion by going over them time and again in your mind.',
                       'Sometimes, we need to accept that bad feelings are occasionally unavoidable and think of ways to make yourself feel better.',
                       'Relax can be a great way to get over negative emotions. Use pleasant activities like reading, walking, or talking to a friend.',
                       'Learn to notice how grief, loss, and anger make you feel, and which events trigger those feelings so you can prepare in advance.',
                       'Exercising or participating in aerobic activity lowers your level of stress chemicals and allows you to cope better with negative emotions.',
                       'Let go of the past, constantly going over negative events robs you of the present and makes you feel bad.'],
                   'sadness': [
                       'Take your mind away from the topic making you sad. Spend some time creating a painting, drawing, or pottery. Create for the sake of creating and do it for yourself.',
                       'Listen to some of your favorite songs that have an upbeat attitude and make you feel happier. The happy music can set up the rest of your day and put a smile on your face.',
                       'Writing in a journal is a great way to cope with your sadness: It acts almost as if you are sharing your thoughts with someone else, except it is private place just for you. It also helps you physically see where your thoughts go so that you can find ways to better understand your thoughts and emotions.',
                       'Be kind to those you see today. Being kind can not only help others, but it also boosts your serotonin levels, biologically making you feel happier',
                       'Sit yourself down with some coffee or tea, a notebook, and have a conversation with yourself. Sometimes we get so caught up trying to learn about the world around us that we completely ignore what is going on inside ourselves.',
                       'If you are feeling sad, get out there and experience a change in scenery. Watch the clouds, take in the trees, and just enjoy a good walk or bike ride. Even if it is just up and down your street, do it.',
                       'Be a little adventurous. Is there something you have wanted to do lately or some place you have always wanted to go but never made the time to go there? Well, now is your chance to do it! Experiencing something new is a great way to put the sadness behind you and put life into a new perspective. Go on an adventure!',
                       'It is okay to cry. A lot of people really hate to cry, but sometimes you just got to cry. All that sadness has got to go somewhere, so let it out.',
                       'A cluttered room can really add on to the negative emotions inside you and make them worse. Try cleaning up or organizing the space around you. It can really help you feel fresh to start off anew.',
                       'Close your eyes. Breathe. Let the thoughts fade out and solely focus on the task of breathing. And you do not even have to meditate on your breathing. You can go outside and focus solely on being outside. You can listen to music and solely focus on that music.'],
                   'disgust': [
                       'Know that feeling bad about ourselves sometimes is a common human experience, and we are not required to be perfect.',
                       'It may not seem like it, but how we sleep and the way we breathe can make a big difference in how we feel. If you feel disgusting, you may not be sleeping enough or breathing deeply. Please let yourself sleep as long at night as you need to feel rested, if you can do so, and please give yourself permission to take naps during the day.',
                       'When we feel disgusting, it is easy to neglect ourselves and engage in other harmful habits. In these times, consider that at the very least, you deserve the same kindness you would show a pet. So, give yourself some nourishing food and water and maybe take yourself out for a walk. Or maybe curl up in bed with a blanket and sleep for a while. You can also give yourself a special treat like you would a pet. Of course, give yourself food and treats appropriate to a human being.',
                       'Pay attention to how the movies, TV shows, and social media accounts you follow make you feel about yourself. It is easy to consume all kinds of media mindlessly. When we do this, we often do not realize when these media influences make us feel bad about ourselves. Unfollow those that make you feel worse and follow those that lift you up',
                       'Several studies suggest that being in nature helps us to feel more kind, compassionate, and creative. When we feel kind, compassionate, and creative, it tends to soften the feelings of disgust we have for ourselves. Take some time with nature to breathe in the fresh air', ],
                   'joy': [
                       'Take time to enjoy the joy you are feeling today! Although these days should come more often, participate in some of your favorite activities to keep the joy flowing to tomorrow.']}

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
        # if it is a positive emotion, send the message - there is only one message for positive emotions
        if len(suggestion_dict[e]) == 1:
            suggestions.append(suggestion_dict[e][0])
        # generate index of suggestion to give if it is a negative emotion
        else:
            index = random.randint(0, len(suggestion_dict[e]) - 1)
            suggestions.append(suggestion_dict[e][index])

    return suggestions

# main method
if __name__ == '__main__':
    for arg in sys.argv[1:]:
        emotions = getSemantics(arg)
        suggestions = giveSuggestions(emotions)

        # create one piece of text that has both
        emotions_w_suggestions = ""
        for i in range(len(emotions)):
            emotions_w_suggestions = emotions_w_suggestions + "|" + emotions[i] + "|" + suggestions[i]

        print(emotions)
        print(suggestions)
        print(emotions_w_suggestions)