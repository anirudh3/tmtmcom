# Identifies Actions the user wants to carry out from the chat

# input - json from NLU, json from Conversation
# output - action number, and associated keyword

# Action number, keyword
# 1 - Play a song, artist, track
# 2 - Recommend, artist, genre
# 3 - Creating a playlist
# 4 -

import random # To random play, recommend things from a regularly updated list

def identifier(conv, nlu):

    ans = {} # dict to store the return answer

    # Check if the intent is to play a track
    if(conv['intents'][0]['intent'] == 'play_a_track'):
        ans['action'] = 1
        if(nlu['entities']):
            ans['keyword'] = nlu['entities'][0]['text']

        else:
            ans['keyword'] = random.choice(["Sam Gellaitry", "San Holo", "John Mayer"])

        return ans

    # CHeck if the intent is to get a recommendation
    if(conv['intents'][0]['intent'] == 'recommend'):
        ans['action'] = 2
        if(nlu['entities']):
            ans['keyword'] = nlu['entities'][0]['text']

        else:
            ans['keyword'] = random.choice(["Sam Gellaitry", "San Holo", "John Mayer"])

        return ans


    # Check if the intent is to create a playlist
