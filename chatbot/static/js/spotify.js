

// Spotify API calls basically depend on particular IDs i.e. - track ID, etc.
// No matter which part we want to access, the idea is to work with these
// unique IDs


// Logging in the user business

// token = util.prompt_for_user_token(username)

// if token:
//     sp = spotipy.Spotify(auth=token)
//     playlists = sp.user_playlists(username)
//     for playlist in playlists['items']:
//         print(playlist['name'])
// else:
//     print("Can't get token for", username)


// Searching for an artist
// Returns : a JSON, comprising of albums by the arist, tracks, and
// metadata for all of it


def search_artist(self, search_str):
    sp = spotipy.Spotify()
    result = sp.search(search_str)  # result contains data in JSON format

    // pprint.pprint(result)


// Getting information about a track, takes in uri - special Spotify ID
// Returns : a JSON, comprising of track info like duration, popularity, 
// and other meta data

def search_track(self, uri):
    sp = spotipy.Spotify()
    track = sp.track(urn)

    // pprint.pprint(track)



// Getting genre recommendations from the database (still need to try this out)
// Returns : a list of suggested tracks in the genre specified

def search_genre(self, gen):
    // gen has to be one of the genres from the available genre list for 
    // recommendations. Get the list by simply calling recommendation_genre_seeds()

    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    sp.trace=False

    results = sp.recommendations(seed_genres = gen)
    // results is a JSON, do whatever with it




// Getting acoustic feature info about a track, takes in track ID
// Stuff like key, tempo, danceability, speechiness, etc, useful to 
// train our Chatbot,
// and maybe even somehow use it to display shit
// Returns : JSON containing duration segments (still don't know why), and info


def get_track_info(self, tid):

    start = time.time()
    features = sp.audio_features(tid)
    delta = time.time() - start
    for feature in features:
        print(json.dumps(feature, indent=4))
        print()
        analysis = sp._get(feature['analysis_url'])
        print(json.dumps(analysis, indent=4))
        print()
    print ("features retrieved in %.2f seconds" % (delta,))
