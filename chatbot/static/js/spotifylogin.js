// Function for parsing the URI to grab the authenticationi key
function parseHash(string){
    var outstr = string.split('=')[1].split('&')[0]

    return(outstr)
}
    

// Function for grabbing the Spotify authentication key from the URI and putting it in local memory

$('document').ready(function(){
    var spotifyAccessToken = parseHash(String(window.location.hash));
    //you must clear localStorage for main page listener to trigger on all(including duplicate) entries
    // localStorage.clear(); Oh, do I now?
    localStorage.setItem('accessToken', spotifyAccessToken);
    window.close();
});


