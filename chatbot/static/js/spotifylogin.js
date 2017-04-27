// Function for parsing the URI to grab the authenticationi key
function parseHash(string){
    var outstr = string.split('=')[1].split('&')[0]

    return(outstr)
}
    
// Createing Cross Site Reference Forgery tokens
function getCSRFToken() {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
        if (cookies[i].startsWith("csrftoken=")) {
            return cookies[i].substring("csrftoken=".length, cookies[i].length);
        }
    }
    return "unknown";
}

// Function for grabbing the Spotify authentication key from the URI and putting it in local memory

$('document').ready(function(){
    var spotifyAccessToken = parseHash(String(window.location.href));
    //you must clear localStorage for main page listener to trigger on all(including duplicate) entries
    localStorage.clear(); //Oh, do I now?
    localStorage.setItem('accessToken', spotifyAccessToken);

    if (spotifyAccessToken == "access_denied"){
        alert("Spotify is returning an Access Denied error.")
    }
    else {
        $.ajax({
            url: "/chatbot/add-spotify-token",
            type: "POST",
            data: "item="+spotifyAccessToken+"&csrfmiddlewaretoken="+getCSRFToken(),
            dataType : "json",
            success: function(response) {
                if (Array.isArray(response)) {
                	window.close();
                    return true;
                } else {
                    alert("Could not get Spotify Token.")
      				window.close();
                    return false;
                }
            }
        });
    }

});


