import random

Hello = ('hello','hey','hii','hi')

reply_Hello = ('Hello Sir , I Am Jarvis .',
            "Hey , What's Up ?",
            "Hey How Are You ?",
            "Hello Sir , Nice To Meet You Again .",
            "Of Course Sir , Hello .")

Bye = ('bye','exit','sleep','go')

reply_bye = ('Bye Sir.',
            "It's Okay .",
            "It Will Be Nice To Meet You .",
            "Bye.",
            "Thanks.",
            "Okay.")

HowAreYou = ('how are you','are you fine')

reply_HowAreYou = ('I Am Fine.',
                  "Excellent .",
                  "Moj Ho rhi Hai .",
                  "Absolutely Fine.",
                  "I'm Fine.",
                  "Thanks For Asking.")

nice = ('nice','good','thanks')

reply_nice = ('Thanks .',
            "Ohh , It's Okay .",
            "Thanks To You.")

Functions = ['functions','abilities','what can you do','features']

reply_Functions = ('I Can Perform Many Task Or Varieties Of Tasks , How Can I Help You ?',
            'I Can Call Your G.F .',
            'I Can Message Your Mom That You Are Not Studing..',
            'I Can Tell Your Class Teacher That You Had Attended All The Online Classes On Insta , Facebbook etc!',
            'Let Me Ask You First , How Can I Help You ?',
            'If You Want Me To Tell My Features , Call : Print Features !')

sorry_reply = ("Sorry sir, I Can't Do That .",
              "sorry sir, i am not able to do that",
              "sorry sir! i really sorry")

def ChatterBot(Text):

    Text = str(Text)

    for word in Text.split():

        if word in Hello:

            reply = random.choice(reply_Hello)

            return reply

        elif word in Bye:

            reply = random.choice(reply_bye)

            return reply
            exit()

        elif word in HowAreYou:

            reply_ = random.choice(reply_HowAreYou)

            return reply_

        elif word in Functions:

            reply___ = random.choice(reply_Functions)

            return reply___

        else:

            return random.choice(sorry_reply)

            

