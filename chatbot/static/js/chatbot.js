// Sends a new request to update the message list
function getList() {
    $.ajax({
        url: "/chatbot/get-list-json",
        dataType : "json",
        success: updateList
    });
}

// Sends a new request to update the search list
function getSearch() {
    $.ajax({
        url: "/chatbot/get-explore-json",
        dataType : "json",
        success: updateExplore
    });
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

// For sanitizing inputs
function sanitize(s) {
    // Be sure to replace ampersand first
    return s.replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;');
}

// For displaying errors
function displayError(message) {
    $("#error").html(message);
}

// For resizing spotify iframes
function resize(){
  $('iframe[src*="embed.spotify.com"]').each( function() {
    $(this).css('width', $(this).parent().css('width'));
    $(this).attr('src', $(this).attr('src'));
    $(this).removeClass('loaded');
    
    $(this).on('load', function(){
      $(this).addClass('loaded');
    });
  });
}

// Adding a user-generated message to the chatbox
function AddChat(){

    var itemTextElement = $("#item");
    var itemTextValue   = itemTextElement.val();

    // Clear input box and old error message (if any)
    itemTextElement.val('');
    displayError('');

    $.ajax({
        url: "/chatbot/add-chat",
        type: "POST",
        data: "item="+itemTextValue+"&csrfmiddlewaretoken="+getCSRFToken(),
        dataType : "json",
        success: function(response) {
            if (Array.isArray(response)) {
                respond();
            } else {
                displayError(response.error);
            }
        }
    });

}


// Changing the drop down Selection for explore to Default
function SetExploreToDefault(){
    document.getElementById("basic-addon1-select").textContent="Selection";
}

// Changing the drop down Selection for explore to Track
function SetExploreToTrack(){
    document.getElementById("basic-addon1-select").textContent="Track";
}

// Changing the drop down Selection for explore to Artist
function SetExploreToArtist(){
    document.getElementById("basic-addon1-select").textContent="Artist";
}

// Changing the drop down Selection for explore to Genre
function SetExploreToGenre(){
    document.getElementById("basic-addon1-select").textContent="Genre";
}

// Changing the drop down Selection for explore to New Music
function SetExploreToPlaylist(){
    document.getElementById("basic-addon1-select").textContent="Playlist";
}

// Searching Explore
function AddExplore(){

    var itemTextElement = $("#item");
    var itemTextValue   = itemTextElement.val();

    var itemSelectValue = $("#basic-addon1-select").text();

    // Clear input box and old error message (if any)
    itemTextElement.val('');
    displayError('');

    
    $.ajax({
        url: "/chatbot/add-explore",
        type: "POST",
        data: "item="+itemTextValue+"%"+itemSelectValue+"&csrfmiddlewaretoken="+getCSRFToken(),
        dataType : "json",
        success: function(response) {
            if (Array.isArray(response)) {
                getSearch();
            } else {
                displayError(response.error);
            }
        }
    });

}

// Getting the top ten tracks for a specific arist
function topTen(uri){

    $.ajax({
        url: "/chatbot/artist-top-ten",
        type: "POST",
        data: "item="+uri+"&csrfmiddlewaretoken="+getCSRFToken(),
        dataType : "json",
        success: function(response) {
            if (Array.isArray(response)) {
                getSearch();
            } else {
                displayError(response.error);
            }
        }
    });
}

// Getting the first 20 tracks in a playlist
function GetPlaylist(uri, userid){
    printf(uri)
    printf(userid)

    $.ajax({
        url: "/chatbot/get-playlist",
        type: "POST",
        data: "item="+uri+"&csrfmiddlewaretoken="+getCSRFToken(),
        dataType : "json",
        success: function(response) {
            if (Array.isArray(response)) {
                getSearch();
            } else {
                displayError(response.error);
            }
        }
    });
}

// Getting the search results for a genre
function SearchGenre(search){
    $.ajax({
        url: "/chatbot/search-genre",
        type: "POST",
        data: "item="+search+"&csrfmiddlewaretoken="+getCSRFToken(),
        dataType : "json",
        success: function(response) {
            if (Array.isArray(response)) {
                getSearch();
            } else {
                displayError(response.error);
            }
        }
    });
}


// Responding to the message of a user
function respond(){
    getList();

    setTimeout(function(){
        $.ajax({
        url: "/chatbot/respond-chat",
        dataType : "json",
        success: getList
        });
    }, 2000);

}

// Updating the list of messages in the chat window
function updateList(listdata){
    mess = jQuery.parseJSON(listdata["mess"])
    chatter = jQuery.parseJSON(listdata["chatter"])

    // Make an array of usernames
    var user_list = {};
    var comm_html = {};

    // $(chatters).each(function() {
    //     var namething = this.fields.name
    //     user_list[this.fields.username] = namething;
    // });

    // Removes the old messages
    $(".chatmess").remove();

    // Adds each new message item to the list
    $(mess).each(function() {
        var chatter_name = chatter[0].fields.name
        if(this.fields.reality_coefficient) {
        
            $("#chat-list").append(

                "<div class='media chatmess'>"+
                    "<img class='d-flex mr-3 img-rounded' width='64px' height='64px' src='../../static/img/egg.png' alt='egg.png'>"+
                    "<div class='media-body'>"+
                        "<div class='row'>"+
                            "<h5 class='mt-0 col-md-1'>"+chatter_name+"</h5>"+
                            "<h7 class='mt-0 col-md-11'>"+ Date(this.fields.created) +"</h7>"+
                        "</div>"+
                        this.fields.text +
                    "</div>"+
                "</div>"+
                "<hr class='chatmess'>"
            );
        }

        else {
        
            $("#chat-list").append(

                "<div class='media chatmess'>"+
                    "<img class='d-flex mr-3 img-rounded' width='64px' height='64px' src='../../static/img/nap.png' alt='egg.png'>"+
                    "<div class='media-body'>"+
                        "<div class='row'>"+
                            "<h5 class='mt-0 col-md-1'> Botto </h5>"+
                            "<h7 class='mt-0 col-md-11'>"+ Date(this.fields.created) +"</h7>"+
                        "</div>"+
                        this.fields.text +
                    "</div>"+
                "</div>"+
                "<hr class='chatmess'>"
            );
        }

    });

    // Scroll to the bottom of the scroll-window
    var objDiv = document.getElementById("scroll-window");

    if (objDiv != null){
        objDiv.scrollTop = objDiv.scrollHeight;
    }

    // Login to spotify if the user is not already logged in
    // console.log(chatter[0].fields.spotify_auth)
    if(chatter[0].fields.spotify_auth == '0'){
        SpotifyLogin();
        // console.log('logged in')
    }
    else{
        // console.log('did not log in')
    }

}

// Test for printing to console
function printf(string){
    console.log(string);
}

// Change the song in the spotify player
function setSong(uri){
    source = "https://embed.spotify.com/?uri=" + uri + "&theme=white";
    document.getElementById('spotifyplayer').src = source;
    resize()
}

// Function for logging in to spotify
function SpotifyLogin(){

    var SPOTIPY_CLIENT_ID = "ba6790bdcd434f06b7b577e344c6e0ae"
    var SPOTIPY_REDIRECT_URI = "http://localhost:8000/chatbot/callback"
    var spotifyScope = "playlist-read-private"
    var state = "GZ2TPEFHXMB4"
    var spotifyAuthEndpoint = "https://accounts.spotify.com/authorize?"+"client_id="+SPOTIPY_CLIENT_ID+"&redirect_uri="+SPOTIPY_REDIRECT_URI+"&scope="+spotifyScope+"&response_type=token&state="+state;
    window.open(spotifyAuthEndpoint,'callBackWindow','height=500,width=400');
    //This event listener will trigger once your callback page adds the token to localStorage
    window.addEventListener("storage",function(event){
        if (event.key == "accessToken"){
            spAccessToken = event.newValue;
            //do things with spotify API using your access token here!!
            CallSpotToken(spAccessToken);
            return true;
        }
        else{
            alert('Did not log in to spotify. Some functionality restrictions will be made.')
            console.log('SpotifyLogin failed')
            return false;
        }
    });
}

// Function for adding spotify token to user
function CallSpotToken(spAccessToken) {
    $.ajax({
        url: "/chatbot/add-spotify-token",
        type: "POST",
        data: "item="+spAccessToken+"&csrfmiddlewaretoken="+getCSRFToken(),
        dataType : "json",
        success: function(response) {
            if (Array.isArray(response)) {
                return true;
            } else {
                alert("Could not get Spotify Token.")
                return false;
            }
        }
    });
}

// Function for getting a popup window in Safari
function PopUp(url, name){
    window.open(url, name, 'height=500,width=400');
}

// Updating the list of search results in the explore Tab
function updateExplore(listdata){
    search = jQuery.parseJSON(listdata["search"]);
    artists = jQuery.parseJSON(listdata["search_artist"]);
    genres = jQuery.parseJSON(listdata["search_genre"]);
    playlists = jQuery.parseJSON(listdata["search_playlist"]);
    // Removes the old messages
    $(".searchres").remove();

    // Adds each new message item to the list
    $(search).each(function() {

        $("#explore-list").append(

                "<tr class='searchres'>"+
                    "<td>"+
                        "<div class='row media'>"+
                            "<div class='col-md-1'>"+
                                "<a href='#' class='pull-left show-image'>"+
                                    "<img src='"+ this.fields.img + "' width='64px' class='media-photo albumart' onclick=\"setSong(" + "\'" + String(this.fields.uri) + "\'" + ")\">"+
                                    "<button class='hidden-button' onclick=\"setSong(" + "\'" + String(this.fields.uri) + "\'" + ")\">Play</button>"+
                                "</a>"+
                            "</div>"+
                            "<div class='col-md-11'>"+
                                "<div class='media-body'>"+
                                    "<span class='media-meta pull-right'>Popularity: " + this.fields.popularity + "</span>"+
                                    "<h4 class='title title-nopad'>"+                                
                                        this.fields.track +
                                    "</h4>"+
                                    "<h5>"+
                                        "<span class='float-right'>"+ this.fields.artist +"</span>"+
                                    "</h5>"+
                                    "<p class='summary'>" + this.fields.album + "</p>"+
                                "</div>"+
                            "</div>"+
                        "</div>"+
                    "</td>"+
                "</tr>"
            );

    });

    // Adds each new artist item to the list
    $(artists).each(function() {

        $("#explore-list").append(

                "<tr class='searchres'>"+
                    "<td>"+
                        "<div class='row media addpad20'>"+
                            "<div class='col-md-1'>"+
                                "<a href='#' class='pull-left show-image'>"+
                                    "<img src='"+ this.fields.img + "' width='64px' class='media-photo albumart' onclick=\"setSong(" + "\'" + String(this.fields.uri) + "\'" + ")\">"+
                                    "<button class='hidden-button' onclick=\"setSong(" + "\'" + String(this.fields.uri) + "\'" + ")\">Play</button>"+
                                "</a>"+
                            "</div>"+
                            "<div class='col-md-11'>"+
                                "<div class='media-body'>"+
                                    "<span class='media-meta pull-right'>Popularity: " + this.fields.popularity + "</span>"+
                                    "<h4 class='title'>"+
                                        "<a onclick=\"topTen(" + "\'" + String(this.fields.uri) + "\'" + ")\" href='#'>"+
                                            this.fields.artist +
                                        "</a>"+
                                    "</h4>"+
                                "</div>"+
                            "</div>"+
                        "</div>"+
                    "</td>"+
                "</tr>"
            );

    });

    // Adds each new artist item to the list
    $(genres).each(function() {

        if(this.fields.genre == 'Try one of these:'){
            $("#explore-list").append(

                "<tr class='searchres'>"+
                    "<td>"+
                        "<div class='row'>"+
                            "<div class='col-md-12'>"+
                                "<div class=''>"+
                                    "<h6 class='subpad20'>"+
                                        this.fields.genre +
                                    "</h6>"+
                                "</div>"+
                            "</div>"+
                        "</div>"+
                    "</td>"+
                "</tr>"
            );
        }
        else{
            $("#explore-list").append(

                "<tr class='searchres'>"+
                    "<td>"+
                        "<div class='row media'>"+
                            "<div class='col-md-12'>"+
                                "<div class='media-body'>"+
                                    "<h4 class='title subpad20'>"+
                                        "<a onclick=\"SearchGenre(" + "\'" + String(this.fields.genre) + "\'" + ")\" href='#'>"+
                                            this.fields.genre +
                                        "</a>"+
                                    "</h4>"+
                                "</div>"+
                            "</div>"+
                        "</div>"+
                    "</td>"+
                "</tr>"
            );
        }

    });

    // Adds each new playlist item to the list
    $(playlists).each(function() {

        $("#explore-list").append(

                "<tr class='searchres'>"+
                    "<td>"+
                        "<div class='row media addpad20'>"+
                            "<div class='col-md-1'>"+
                                "<a href='#' class='pull-left show-image'>"+
                                    "<img src='"+ this.fields.img + "' width='64px' class='media-photo albumart' onclick=\"setSong(" + "\'" + String(this.fields.uri) + "\'" + ")\">"+
                                    "<button class='hidden-button' onclick=\"setSong(" + "\'" + String(this.fields.uri) + "\'" + ")\">Play</button>"+
                                "</a>"+
                            "</div>"+
                            "<div class='col-md-11'>"+
                                "<div class='media-body'>"+
                                    "<span class='media-meta pull-right'>Followers: " + this.fields.followers + "</span>"+
                                    "<h4 class='title'>"+
                                        "<a onclick=\"GetPlaylist(" + "\'" + String(this.fields.uri) + "\'" +", " +"\'" + String(this.fields.ownerid) + "\'" + ")\" href='#'>"+
                                            this.fields.playlist +
                                        "</a>"+
                                    "</h4>"+
                                    "<h5>"+
                                        "<span class='float-right'>"+ this.fields.owner +"</span>"+
                                    "</h5>"+
                                    "<p class='summary'>Tracks: " + this.fields.trackcount + "</p>"+
                                "</div>"+
                            "</div>"+
                        "</div>"+
                    "</td>"+
                "</tr>"
            );

    });

    // Scroll to the bottom of the scroll-window

}

// Automatically change the spotify player size when you resize the screen
$(window).on('load resize', function() {
  $('iframe[src*="embed.spotify.com"]').each( function() {
    $(this).css('width', $(this).parent().css('width'));
    $(this).attr('src', $(this).attr('src'));
    $(this).removeClass('loaded');
    
    $(this).on('load', function(){
      $(this).addClass('loaded');
    });
  });
});

// The index.html does not load the list, so we call getList()
// as soon as page is finished loading
$(window).on('load', function() {
    getList();

// causes list to be re-fetched every 5 seconds
// window.setInterval(getList, 5000);
});



