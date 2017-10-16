

// Sends a new request to update the message list
function getList() {
    $.ajax({
        url: "/chatbot/get-list-json",
        dataType : "json",
        success: updateList //Apparently you CAN NOT put parantheses here
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

// Sends a new request to update the search list
function getObserve(location) {
    $.ajax({
        url: "/chatbot/get-observe-json",
        dataType : "json",
        success: updateObserve
    });
}

// Sends a new request to update the search list for location based requests
function getObserve2(location) {
    $.ajax({
        url: "/chatbot/get-observe-json2",
        type: "POST",
        data: "item="+location+"&csrfmiddlewaretoken="+getCSRFToken(),
        dataType : "json",
        success: updateObserve
    });
}

// Sends a new request to upate the user's top music list
function getYou() {
    $.ajax({
        url: "/chatbot/get-you-json",
        dataType : "json",
        success: updateYou
    });
}

// Sends a new request to get all the city info
function getCity() {
    $.ajax({
        url: "/chatbot/get-city-json",
        dataType : "json",
        success: updateCity
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

// Check if the user is currently logged into spotify, if not alert that functionality will be restricted
function SpotifyAlert(){
    alert("You have not logged into Spotify. Please do so in the Settings tab to use this function.")
}

// Function to change the tabs to do what they are supposed to do.
function setSpotifyLinks(){
    document.getElementById("chattab").onclick = '';
    document.getElementById("exploretab").onclick = '';
    document.getElementById("youtab").onclick = '';

    document.getElementById("chattab").href = '/chatbot/chat';
    document.getElementById("exploretab").href = '/chatbot/observe';
    document.getElementById("youtab").href = '/chatbot/you';
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

// Displaying the info about tabs in new windows
function dispInfoHunt(){
    // print("displayInfoHunt called")
    huntinfoURL = '/chatbot/gethuntinfo'
    window.open(huntinfoURL,'Hunt Tab Info','height=500,width=400');
}

function dispExploreHunt(){
    // print("yaya")

    exploreinfoURL = '/chatbot/getexploreinfo'
    window.open(exploreinfoURL,'Explore Tab Info','height=700,width=400');
}

// Changing the drop down Selection for explore to Default
function SetExploreToDefault(){
    document.getElementById("explore-select").textContent="Hunt By...";
}

// Changing the drop down Selection for explore to Track
function SetExploreToTrack(){
    document.getElementById("explore-select").textContent="Track";
}

// Changing the drop down Selection for explore to Artist
function SetExploreToArtist(){
    document.getElementById("explore-select").textContent="Artist";
}

// Changing the drop down Selection for explore to Genre
function SetExploreToGenre(){
    document.getElementById("explore-select").textContent="Genre";
}

// Changing the drop down Selection for explore to New Music
function SetExploreToPlaylist(){
    document.getElementById("explore-select").textContent="Playlist";
}

// Changing the drop down Selection for observe to Default
function SetObserveToDefault(){
    SetParamDefault();
    turnValOff();
    document.getElementById("observe-text").value = "";
    document.getElementById("observe-text").placeholder = "For searching by tag.";
    document.getElementById("observe-text").disabled = true;
    document.getElementById("observe-select").textContent="Explore by...";
    document.getElementById("param-select").textContent="Parameter";
}

// Changing the drop down Selection for observe to Location
function SetObserveToLocation(){
    getCity()
    turnValOff();
    $(".searchres").remove();
    document.getElementById("observe-text").placeholder = "For searching by tag.";
    document.getElementById("observe-text").disabled = true;
    document.getElementById("observe-select").textContent="Location";
}

// Changing the drop down Selection for observe to Tag
function SetObserveToTag(){
    SetParamTag()
    turnValOn();
    $(".searchres").remove();
    document.getElementById("observe-text").placeholder = "Search for tracks similar to...";
    document.getElementById("observe-text").disabled = false;
    document.getElementById("observe-select").textContent="Tag";
}

// Changing the drop down value selection for observe to Default
function SetValToDefault(){
    var elementExists = document.getElementById("value-select");
    if (elementExists){
        document.getElementById("value-select").textContent="Value";
    }

}

// Changing the drop down value selection for observe
function SetValTo(string){
    document.getElementById("value-select").textContent=string;
}

// Changing the drop down parameter selection for observe
function SetParamTo(string){
    SetValToDefault();
    var itemSelectValue = $("#observe-select").text();

    if (itemSelectValue == "Location"){
        string = string.split(',')[0]
    }

    document.getElementById("param-select").textContent=string;

    switch(string){
        case 'Acousticness':
            setValDigit();
            break;
        case 'Danceability':
            setValDigit();
            break;
        case 'Energy':
            setValDigit();
            break;
        case 'Instrumentalness':
            setValDigit();
            break;
        case 'Key':
            setValKey();
            break;
        case 'Liveness':
            setValDigit();
            break;
        case 'Loudness':
            setValDigit();
            break;
        case 'Speechiness':
            setValDigit();
            break;
        case 'Tempo':
            setValTempo();
            break;
        case 'Time Signature':
            setValTime();
            break;
        case 'Valence':
            setValDigit();
            break;
    }

}

// Populating the parameter selection drop down to default
function SetParamDefault(){
    // Removes the old messages
    $(".paramenu").remove();

    $("#paramenu-set").append(
        "<p class='dropdown-item paramenu' href='#'>Choose an observation first.</p>"
    );
}


// Populating the parameter selection drop down to Tags
function SetParamTag(){
    // Removes the old messages
    $(".paramenu").remove();

    $("#paramenu-set").append(
        '<li><a class="dropdown-item paramenu" href="#"" onclick=' + '\"' + 'SetParamTo(' + '\'' + 'Acousticness' + '\'' + ');' + '\"' + '><h5>Acousticness</h5></a></li>'+
        '<li><a class="dropdown-item paramenu" href="#"" onclick=' + '\"' + 'SetParamTo(' + '\'' + 'Danceability' + '\'' + ');' + '\"' + '><h5>Danceability</h5></a></li>'+
        '<li><a class="dropdown-item paramenu" href="#"" onclick=' + '\"' + 'SetParamTo(' + '\'' + 'Energy' + '\'' + ');' + '\"' + '><h5>Energy</h5></a></li>'+
        '<li><a class="dropdown-item paramenu" href="#"" onclick=' + '\"' + 'SetParamTo(' + '\'' + 'Instrumentalness' + '\'' + ');' + '\"' + '><h5>Instrumentalness</h5></a></li>'+
        '<li><a class="dropdown-item paramenu" href="#"" onclick=' + '\"' + 'SetParamTo(' + '\'' + 'Key' + '\'' + ');' + '\"' + '><h5>Key</h5></a></li>'+
        '<li><a class="dropdown-item paramenu" href="#"" onclick=' + '\"' + 'SetParamTo(' + '\'' + 'Liveness' + '\'' + ');' + '\"' + '><h5>Liveness</h5></a></li>'+
        '<li><a class="dropdown-item paramenu" href="#"" onclick=' + '\"' + 'SetParamTo(' + '\'' + 'Loudness' + '\'' + ');' + '\"' + '><h5>Loudness</h5></a></li>'+
        '<li><a class="dropdown-item paramenu" href="#"" onclick=' + '\"' + 'SetParamTo(' + '\'' + 'Speechiness' + '\'' + ');' + '\"' + '><h5>Speechiness</h5></a></li>'+
        '<li><a class="dropdown-item paramenu" href="#"" onclick=' + '\"' + 'SetParamTo(' + '\'' + 'Tempo' + '\'' + ');' + '\"' + '><h5>Tempo</h5></a></li>'+
        '<li><a class="dropdown-item paramenu" href="#"" onclick=' + '\"' + 'SetParamTo(' + '\'' + 'Time Signature' + '\'' + ');' + '\"' + '><h5>Time Signature</h5></a></li>'+
        '<li><a class="dropdown-item paramenu" href="#"" onclick=' + '\"' + 'SetParamTo(' + '\'' + 'Valence' + '\'' + ');' + '\"' + '><h5>Valence</h5></a></li>'
    );
}

// Updating the You tab
function AddYou(){
    $.ajax({
        url: "/chatbot/add-you",
        type: "POST",
        data: "&csrfmiddlewaretoken="+getCSRFToken(),
        dataType: "json",
        success: function(response){
            if (Array.isArray(response)) {
                getYou();
            } else {
                displayError(response.error)
            }
        }
    });
}

// Searching Observe
function AddObserve(){

    var itemTextElement = $("#observe-text");
    var itemTextValue   = itemTextElement.val();

    var itemSelectValue = $("#observe-select").text();
    var itemSelectParam = $("#param-select").text();

    // Clear input box and old error message (if any)
    itemTextElement.val('');
    displayError('');

    if(itemSelectValue == "Explore by..." & itemSelectParam == "Parameter"){
        alert("You must select to explore by either location or tag.");
    }
    else if(itemSelectValue == "Location" & itemSelectParam == "Parameter"){
        alert("You must choose a location to explore by location.")
    }
    else if(!itemTextValue & itemSelectValue == "Tag"){
        alert("You must search for a song to explore similar songs!")
    }

    else {

        // Removes the old messages
        $(".searchres").remove();


        $("#observe-list").append(

            "<tr class='searchres'>"+
                "<td>"+
                    "<div class='row media addpad20'>"+
                        "<div class='col-md-11'>"+
                            "<div class='media-body'>"+
                                "<p class='summary'>Searching!</p>"+
                            "</div>"+
                        "</div>"+
                    "</div>"+
                "</td>"+
            "</tr>"
        );

        if(itemSelectValue == "Location"){
            $.ajax({
                url: "/chatbot/add-observe",
                type: "POST",
                data: "item="+itemTextValue+"~"+itemSelectValue+"~"+itemSelectParam+"&csrfmiddlewaretoken="+getCSRFToken(),
                dataType : "json",
                success: function(response) {
                    if (Array.isArray(response)) {
                        getObserve2(itemSelectParam);
                    } else {
                        displayError(response.error);
                    }
                }
            });
        }
        else if(itemSelectValue == "Tag"){

            // Removes the old messages
            $(".searchres").remove();


            $("#observe-list").append(

                "<tr class='searchres'>"+
                    "<td>"+
                        "<div class='row media addpad20'>"+
                            "<div class='col-md-11'>"+
                                "<div class='media-body'>"+
                                    "<p class='summary'>Searching!</p>"+
                                "</div>"+
                            "</div>"+
                        "</div>"+
                    "</td>"+
                "</tr>"
            );

            $.ajax({
                url: "/chatbot/add-observe",
                type: "POST",
                data: "item="+itemTextValue+"~"+itemSelectValue+"~"+itemSelectParam+"&csrfmiddlewaretoken="+getCSRFToken(),
                dataType : "json",
                success: function(response) {
                    if (Array.isArray(response)) {
                        getObserve();
                    } else {
                        displayError(response.error);
                    }
                }
            });
        }
    }
}


// Searching Explore
function AddExplore(){

    var itemTextElement = $("#item");
    var itemTextValue   = itemTextElement.val();

    var itemSelectValue = $("#explore-select").text();

    // Clear input box and old error message (if any)
    itemTextElement.val('');
    displayError('');

    if (itemTextValue.indexOf(';') > -1){
        alert("Please do not use special characters in the search.")
    }
    else if (itemSelectValue == "Hunt By..."){
        alert("You must choose a selection to hunt by.")
    }
    else if (!itemTextValue){
        alert("You must input something to search by.")
    }
    else {
        // Removes the old messages
        $(".searchres").remove();


        $("#explore-list").append(

            "<tr class='searchres'>"+
                "<td>"+
                    "<div class='row media addpad20'>"+
                        "<div class='col-md-11'>"+
                            "<div class='media-body'>"+
                                "<p class='summary'>Searching!</p>"+
                            "</div>"+
                        "</div>"+
                    "</div>"+
                "</td>"+
            "</tr>"
        );

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
// Finding relavent track for recommendations
function recommendTrack(uri){

    var itemSelectValue = $("#value-select").text();
    var itemSelectParam = $("#param-select").text();

    console.log("Item Select Value")
    console.log(itemSelectValue)
    console.log("Item Select Param")
    console.log(itemSelectParam)

    if (itemSelectValue == "Value" || itemSelectParam == "Parameter"){
        alert("You must choose a tag and value to explore songs.")
    }
    else{
        // Removes the old messages
        $(".searchres").remove();


        $("#observe-list").append(

            "<tr class='searchres'>"+
                "<td>"+
                    "<div class='row media addpad20'>"+
                        "<div class='col-md-11'>"+
                            "<div class='media-body'>"+
                                "<p class='summary'>Searching!</p>"+
                            "</div>"+
                        "</div>"+
                    "</div>"+
                "</td>"+
            "</tr>"
        );

        $.ajax({
            url: "/chatbot/recommend-track",
            type: "POST",
            data: "item="+uri+"~"+itemSelectValue+"~"+itemSelectParam+"&csrfmiddlewaretoken="+getCSRFToken(),
            dataType : "json",
            success: function(response) {
                if (Array.isArray(response)) {
                    getObserve();
                } else {
                    displayError(response.error);
                }
            }
        });
    }


}


// Getting the first 20 tracks in a playlist
function GetPlaylist(uri, userid){
    // printf(uri)
    // printf(userid)


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
    // Focus on input
    var elementExists = document.getElementById("item");
    if (elementExists){
        document.getElementById("item").focus();
    }

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

    // // Login to spotify if the user is not already logged in
    // // console.log(chatter[0].fields.spotify_auth)
    // if(chatter[0].fields.spotify_auth == '0'){
    //     SpotifyLogin();
    //     // console.log('logged in')
    // }
    // else{
    //     // console.log('did not log in')
    // }

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
    // var SPOTIPY_REDIRECT_URI = "http://talkmusictome.com/chatbot/callback"
    var SPOTIPY_REDIRECT_URI = "http://localhost:8000/chatbot/callback"
    var spotifyScope = "playlist-read-private user-top-read playlist-modify-public playlist-modify-private"
    var state = "GZ2TPEFHXMB4"
    var show_dialog = "true"
    var spotifyAuthEndpoint = "https://accounts.spotify.com/authorize?"+"client_id="+SPOTIPY_CLIENT_ID+"&redirect_uri="+SPOTIPY_REDIRECT_URI+"&scope="+spotifyScope+"&response_type=token&state="+state+"&show_dialog="+show_dialog;

    $.ajax({
         url: '/chatbot/settings',
         type: 'GET',
         success: function(){

            window.open(spotifyAuthEndpoint,'callBackWindow','height=500,width=400');

        },
         async: false
    });
}

// Check if the user is logged in
function checkIfLoggedIn(listdata){
    chatter = jQuery.parseJSON(listdata["chatter"]);
    var elementExists = document.getElementById("f-firstname");
    if (elementExists){
        document.getElementById("f-firstname").placeholder=chatter[0].fields.fname;
    }

    var elementExists = document.getElementById("f-lastname");
    if (elementExists){
        document.getElementById("f-lastname").placeholder=chatter[0].fields.lname;
    }

    var elementExists = document.getElementById("f-age");
    if (elementExists){
        if (chatter[0].fields.age.length > 0){
            document.getElementById("f-age").placeholder=chatter[0].fields.age;
        }
    }
    var elementExists = document.getElementById("f-email");
    if (elementExists){
        document.getElementById("f-email").placeholder=chatter[0].fields.email;
    }

    var elementExists = document.getElementById("f-location");
    if (elementExists){
        document.getElementById("f-location").selectedIndex= Number(chatter[0].fields.location);
    }

    // console.log(chatter[0].fields.spority_auth)
    if (chatter[0].fields.spotify_auth == '0'){
        // console.log("not logged in")
        // Remove hunt by genre from selection list
        var elementExists = document.getElementById("huntforgenre");
        if (elementExists){
            $(".huntforgenre").remove();
        }

        // Dissalow clicking on playlists
        elementArray = document.getElementsByClassName("playlistscript");

        if (elementArray.length){
            for(var i = 0; i < elementArray.length; i++)
            {
                // PERFORM STUFF ON THE ELEMENT
                elementArray[i].onclick = function(){SpotifyAlert};
            }
        }


    }
    else{
        // console.log("logged in")
        // Sets the links for the tabs to the standard ones.
        setSpotifyLinks();

        var elementExists = document.getElementById("logged_in");
        if (elementExists){
            document.getElementById("logged_in").textContent="Logged in";
        }
    }
}

// Function for getting a popup window in Safari
function PopUp(url, name){
    window.open(url, name, 'height=500,width=400');
}

// Update the city information in the Observe tab
function updateCity(listdata){
    chatter = jQuery.parseJSON(listdata["chatter"]);
    countlist = listdata["countlist"];
    cities = [];

    for (i = 0; i < 380; i++){
        city = listdata[i];
        cities[i] = city;
    }

    // Removes the old messages
    $(".paramenu").remove();

    for (i = 0; i < 380; i++){

        if(countlist[i] > 0){
            $("#paramenu-set").append(
                '<li><a class="dropdown-item paramenu" href="#"" onclick=' + '\"' + 'SetParamTo(' + '\'' + cities[i] + '\'' + ');' + '\"' + '><h6>'+ cities[i] + ' - Users: '+ countlist[i] +'</h6></a></li>'
            );
        }
    }
}

// Add the dropdown menu for parameter values
function turnValOn(){

    // Removes the old messages
    $(".dropdown-value").remove();

    $("#dropdown-value").append(
        '<button type="button" class="btn btn-outline-primary dropdown-value dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" id="value-select">Value<span class="caret"></span></button>'+
            '<ul class="dropdown-menu scrollable-menu dropdown-value" role="menu">'+
                '<div id="valmenu-set">'+
                    '<div class="valmenu-set">'+
                        '<p class="dropdown-item dropdown-value" href="#">Choose a parameter first.</p>'+
                    '</div>'+
                '</div>'+
            '</ul>'+
        '</button>'
    )
}

// Remove the dropdown menu for parameter values
function turnValOff(){
    // Removes the old messages
    $(".dropdown-value").remove();
}

// Change the value selection to digits from 0 to 1
function setValDigit(){

    // Removes the old messages
    $(".valmenu-set").remove();

    for (var i = 0; i < 21; i++) {

        $("#valmenu-set").append(
            '<li><a class="dropdown-item valmenu-set" href="#"" onclick=' + '\"' + 'SetValTo(' + '\'' + String(i*5) + '%' + '\'' + ');' + '\"' + '><h5>'+ String(i*5) +'%</h5></a></li>'
        )
    }
}

// Change the value selection to keys
function setValKey(){

    // Removes the old messages
    $(".valmenu-set").remove();

    $("#valmenu-set").append(
        '<li><a class="dropdown-item valmenu-set" href="#"" onclick=' + '\"' + 'SetValTo(' + '\'' + 'C' + '\'' + ');' + '\"' + '><h5>C</h5></a></li>'+
        '<li><a class="dropdown-item valmenu-set" href="#"" onclick=' + '\"' + 'SetValTo(' + '\'' + 'C♯/D♭' + '\'' + ');' + '\"' + '><h5>C♯/D♭</h5></a></li>'+
        '<li><a class="dropdown-item valmenu-set" href="#"" onclick=' + '\"' + 'SetValTo(' + '\'' + 'D' + '\'' + ');' + '\"' + '><h5>D</h5></a></li>'+
        '<li><a class="dropdown-item valmenu-set" href="#"" onclick=' + '\"' + 'SetValTo(' + '\'' + 'D♯/E♭' + '\'' + ');' + '\"' + '><h5>D♯/E♭</h5></a></li>'+
        '<li><a class="dropdown-item valmenu-set" href="#"" onclick=' + '\"' + 'SetValTo(' + '\'' + 'E' + '\'' + ');' + '\"' + '><h5>E</h5></a></li>'+
        '<li><a class="dropdown-item valmenu-set" href="#"" onclick=' + '\"' + 'SetValTo(' + '\'' + 'F' + '\'' + ');' + '\"' + '><h5>F</h5></a></li>'+
        '<li><a class="dropdown-item valmenu-set" href="#"" onclick=' + '\"' + 'SetValTo(' + '\'' + 'F♯/G♭' + '\'' + ');' + '\"' + '><h5>F♯/G♭</h5></a></li>'+
        '<li><a class="dropdown-item valmenu-set" href="#"" onclick=' + '\"' + 'SetValTo(' + '\'' + 'G' + '\'' + ');' + '\"' + '><h5>G</h5></a></li>'+
        '<li><a class="dropdown-item valmenu-set" href="#"" onclick=' + '\"' + 'SetValTo(' + '\'' + 'G♯/A♭' + '\'' + ');' + '\"' + '><h5>G♯/A♭</h5></a></li>'+
        '<li><a class="dropdown-item valmenu-set" href="#"" onclick=' + '\"' + 'SetValTo(' + '\'' + 'A' + '\'' + ');' + '\"' + '><h5>A</h5></a></li>'+
        '<li><a class="dropdown-item valmenu-set" href="#"" onclick=' + '\"' + 'SetValTo(' + '\'' + 'A♯/B♭' + '\'' + ');' + '\"' + '><h5>A♯/B♭</h5></a></li>'+
        '<li><a class="dropdown-item valmenu-set" href="#"" onclick=' + '\"' + 'SetValTo(' + '\'' + 'B' + '\'' + ');' + '\"' + '><h5>B</h5></a></li>'
    )


}

// Change the value selection to tempos
function setValTempo(){
    // Removes the old messages
    $(".valmenu-set").remove();

    for (var i = 0; i < 29; i++) {

        $("#valmenu-set").append(
            '<li><a class="dropdown-item valmenu-set" href="#"" onclick=' + '\"' + 'SetValTo(' + '\'' + String(i*5 + 60) + ' bpm' + '\'' + ');' + '\"' + '><h5>'+ String(i*5 + 60) +' bpm</h5></a></li>'
        )
    }
}

// Change the value selection to time signitures
function setValTime(){
    // Removes the old messages
    $(".valmenu-set").remove();

    for (var i = 2; i < 10; i++) {

        $("#valmenu-set").append(
            '<li><a class="dropdown-item valmenu-set" href="#"" onclick=' + '\"' + 'SetValTo(' + '\'' + String(i) + '/4' + '\'' + ');' + '\"' + '><h5>'+ String(i) +'/4</h5></a></li>'
        )
    }
}

// Update the personal data for the You tab
function updateYou(listdata){
    checkIfLoggedIn(listdata);
    tracks = jQuery.parseJSON(listdata["tracks"]);
    artists = jQuery.parseJSON(listdata["artists"]);
    chatter = jQuery.parseJSON(listdata["chatter"]);
    genres = jQuery.parseJSON(listdata["genres"]);

    avgkey = chatter[0].fields.key.toFixed(0)

    switch(avgkey){
        case '0':
            avgkey = 'C'
            break;
        case '1':
            avgkey = 'C♯/D♭'
            break;
        case '2':
            avgkey = 'D'
            break;
        case '3':
            avgkey = 'D♯/E♭'
            break;
        case '4':
            avgkey = 'E'
            break;
        case '5':
            avgkey = 'F'
            break;
        case '6':
            avgkey = 'F♯/G♭'
            break;
        case '7':
            avgkey = 'G'
            break;
        case '8':
            avgkey = 'G♯/A♭'
            break;
        case '9':
            avgkey = 'A'
            break;
        case '10':
            avgkey = 'A♯/B♭'
            break;
        case '11':
            avgkey = 'B'
        // default:
        //     avgkey = 'Couldn\'t find a key'
    }

    // Remove old top songs
    $(".topsongs").remove();
    var count = 0
    // Adds each new Song item into the list
    $(tracks).each(function(){

        $("#you-slist").append(


            "<tr class='topsongs'>"+
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
    count = count + 1
    });

    // Remove old top artists
    $(".topartists").remove();

    // Adds each new Artist item into the list
    $(artists).each(function(){

        $("#you-alist").append(

            "<tr class='topartists'>"+
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
                                    "<a onclick=\"setSong(" + "\'" + String(this.fields.uri) + "\'" + ")\" href='#'>"+
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

    // Remove old top artists
    $(".topgenres").remove();

    $("#you-glist").append(

        "<tr class='topgenres'>"+
            "<td>"+
                "<div class='row'>"+
                    "<div class='col-md-12'>"+
                        "<div class=''>"+
                            "<h3 class='subpad20'>"+
                                "Your Top Genres"+
                            "</h3>"+
                        "</div>"+
                    "</div>"+
                "</div>"+
            "</td>"+
        "</tr>"

    );

    // Adds each new Artist item into the list
    $(genres).each(function(){

        $("#you-glist").append(

            "<tr class='topgenres'>"+
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
    });

    // Remove old top artists
    $(".toptags").remove();

    $("#you-tlist").append(

        "<tr class='toptags'>"+
            "<td>"+
                "<div class='row'>"+
                    "<div class='col-md-12'>"+
                        "<div class=''>"+
                            "<h3 class='subpad20'>"+
                                "Your Average Spotify Meta-Data"+
                            "</h3>"+
                        "</div>"+
                    "</div>"+
                "</div>"+
            "</td>"+
        "</tr>"

    );

    // Adding Acousticness
    $("#you-tlist").append(

        "<tr class='toptags'>"+
            "<td>"+
                "<div class='row'>"+
                    "<div class='col-md-12'>"+
                        "<div class=''>"+
                            "<h5 class='subpad20'>"+
                                "Acousticness: "+
                                chatter[0].fields.acousticness.toFixed(2) +
                            "</h5>"+
                            "<h6>"+
                                "A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic."+
                            "</h6>"+
                        "</div>"+
                    "</div>"+
                "</div>"+
            "</td>"+
        "</tr>"

    );

    // Adding Danceability
    $("#you-tlist").append(

        "<tr class='toptags'>"+
            "<td>"+
                "<div class='row'>"+
                    "<div class='col-md-12'>"+
                        "<div class=''>"+
                            "<h5 class='subpad20'>"+
                                "Danceability: "+
                                chatter[0].fields.danceability.toFixed(2) +
                            "</h5>"+
                            "<h6>"+
                                "Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity."+
                            "</h6>"+
                        "</div>"+
                    "</div>"+
                "</div>"+
            "</td>"+
        "</tr>"

    );

    // Adding Energy
    $("#you-tlist").append(

        "<tr class='toptags'>"+
            "<td>"+
                "<div class='row'>"+
                    "<div class='col-md-12'>"+
                        "<div class=''>"+
                            "<h5 class='subpad20'>"+
                                "Energy: "+
                                chatter[0].fields.energy.toFixed(2) +
                            "</h5>"+
                            "<h6>"+
                                "Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy."+
                            "</h6>"+
                        "</div>"+
                    "</div>"+
                "</div>"+
            "</td>"+
        "</tr>"

    );

    // Adding Instrumentalness
    $("#you-tlist").append(

        "<tr class='toptags'>"+
            "<td>"+
                "<div class='row'>"+
                    "<div class='col-md-12'>"+
                        "<div class=''>"+
                            "<h5 class='subpad20'>"+
                                "Instrumentalness: "+
                                chatter[0].fields.instrumentalness.toFixed(2) +
                            "</h5>"+
                            "<h6>"+
                                "Predicts whether a track contains no vocals. \"Ooh\" and \"aah\" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly \"vocal\". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. "+
                            "</h6>"+
                        "</div>"+
                    "</div>"+
                "</div>"+
            "</td>"+
        "</tr>"

    );

    // Adding Key
    $("#you-tlist").append(

        "<tr class='toptags'>"+
            "<td>"+
                "<div class='row'>"+
                    "<div class='col-md-12'>"+
                        "<div class=''>"+
                            "<h5 class='subpad20'>"+
                                "Key: "+
                                avgkey +
                            "</h5>"+
                            "<h6>"+
                                "The key the track is in."+
                            "</h6>"+
                        "</div>"+
                    "</div>"+
                "</div>"+
            "</td>"+
        "</tr>"

    );

    // Adding Liveness
    $("#you-tlist").append(

        "<tr class='toptags'>"+
            "<td>"+
                "<div class='row'>"+
                    "<div class='col-md-12'>"+
                        "<div class=''>"+
                            "<h5 class='subpad20'>"+
                                "Liveness: "+
                                chatter[0].fields.liveness.toFixed(2) +
                            "</h5>"+
                            "<h6>"+
                                "Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live."+
                            "</h6>"+
                        "</div>"+
                    "</div>"+
                "</div>"+
            "</td>"+
        "</tr>"

    );

    // Adding Loudness
    $("#you-tlist").append(

        "<tr class='toptags'>"+
            "<td>"+
                "<div class='row'>"+
                    "<div class='col-md-12'>"+
                        "<div class=''>"+
                            "<h5 class='subpad20'>"+
                                "Loudness: "+
                                chatter[0].fields.loudness.toFixed(2) +
                            "</h5>"+
                            "<h6>"+
                                "The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks."+
                            "</h6>"+
                        "</div>"+
                    "</div>"+
                "</div>"+
            "</td>"+
        "</tr>"

    );

    // Adding Speechiness
    $("#you-tlist").append(

        "<tr class='toptags'>"+
            "<td>"+
                "<div class='row'>"+
                    "<div class='col-md-12'>"+
                        "<div class=''>"+
                            "<h5 class='subpad20'>"+
                                "Speechiness: "+
                                chatter[0].fields.speechiness.toFixed(2) +
                            "</h5>"+
                            "<h6>"+
                                "Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value."+
                            "</h6>"+
                        "</div>"+
                    "</div>"+
                "</div>"+
            "</td>"+
        "</tr>"

    );

    // Adding Tempo
    $("#you-tlist").append(

        "<tr class='toptags'>"+
            "<td>"+
                "<div class='row'>"+
                    "<div class='col-md-12'>"+
                        "<div class=''>"+
                            "<h5 class='subpad20'>"+
                                "Tempo: "+
                                chatter[0].fields.tempo.toFixed(2) +
                            "</h5>"+
                            "<h6>"+
                                "The overall estimated tempo of a track in beats per minute (BPM)."+
                            "</h6>"+
                        "</div>"+
                    "</div>"+
                "</div>"+
            "</td>"+
        "</tr>"

    );

    // Adding Time_signature
    $("#you-tlist").append(

        "<tr class='toptags'>"+
            "<td>"+
                "<div class='row'>"+
                    "<div class='col-md-12'>"+
                        "<div class=''>"+
                            "<h5 class='subpad20'>"+
                                "Time Signature: "+
                                chatter[0].fields.time_signature.toFixed(1) +
                            "</h5>"+
                            "<h6>"+
                                "An estimated overall time signature of a track."+
                            "</h6>"+
                        "</div>"+
                    "</div>"+
                "</div>"+
            "</td>"+
        "</tr>"

    );

    // Adding Valence
    $("#you-tlist").append(

        "<tr class='toptags'>"+
            "<td>"+
                "<div class='row'>"+
                    "<div class='col-md-12'>"+
                        "<div class=''>"+
                            "<h5 class='subpad20'>"+
                                "Valence: "+
                                chatter[0].fields.valence.toFixed(2) +
                            "</h5>"+
                            "<h6>"+
                                "A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry)."+
                            "</h6>"+
                        "</div>"+
                    "</div>"+
                "</div>"+
            "</td>"+
        "</tr>"

    );

    // Scroll to the top of the scroll-window
    var objDiv = document.getElementById("tags");

    if (objDiv != null){
        objDiv.scrollTop = 0;
    }

    // Scroll to the top of the scroll-window
    var objDiv = document.getElementById("artists");

    if (objDiv != null){
        objDiv.scrollTop = 0;
    }

    // Scroll to the top of the scroll-window
    var objDiv = document.getElementById("genres");

    if (objDiv != null){
        objDiv.scrollTop = 0;
    }

    // Scroll to the top of the scroll-window
    var objDiv = document.getElementById("songs");

    if (objDiv != null){
        objDiv.scrollTop = 0;
    }

}

// Updating the list of search results in the observe Tab
function updateObserve(listdata){
    search = jQuery.parseJSON(listdata["search"]);
    htracks = jQuery.parseJSON(listdata["htracks"])

    var itemSelectParam = $("#param-select").text();
    var itemSelectType = $("#observe-select").text();
    var strinfo = '';

    console.log(htracks)

    // Removes the old messages
    $(".searchres").remove();

    if (itemSelectType == "Tag"){

        // Adds each new message item to the list
        $(search).each(function() {

            switch(itemSelectParam){
                case 'Acousticness':
                    strinfo = ' - ' + String(itemSelectParam) + ': ' + String(this.fields.acousticness);
                    break;
                case 'Danceability':
                    strinfo = ' - ' + String(itemSelectParam) + ': ' + String(this.fields.danceability);
                    break;
                case 'Energy':
                    strinfo = ' - ' + String(itemSelectParam) + ': ' + String(this.fields.energy);
                    break;
                case 'Instrumentalness':
                    strinfo = ' - ' + String(itemSelectParam) + ': ' + String(this.fields.instrumentalness);
                    break;
                case 'Key':
                    strinfo = ' - ' + String(itemSelectParam) + ': ' + String(this.fields.key);
                    break;
                case 'Liveness':
                    strinfo = ' - ' + String(itemSelectParam) + ': ' + String(this.fields.liveness);
                    break;
                case 'Loudness':
                    strinfo = ' - ' + String(itemSelectParam) + ': ' + String(this.fields.loudness);
                    break;
                case 'Speechiness':
                    strinfo = ' - ' + String(itemSelectParam) + ': ' + String(this.fields.speechiness);
                    break;
                case 'Tempo':
                    strinfo = ' - ' + String(itemSelectParam) + ': ' + String(this.fields.tempo);
                    break;
                case 'Time Signature':
                    strinfo = ' - ' + String(itemSelectParam) + ': ' + String(this.fields.time_signature);
                    break;
                case 'Valence':
                    strinfo = ' - ' + String(itemSelectParam) + ': ' + String(this.fields.valence);
                    break;
            }


            $("#observe-list").append(

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
                                    "<span class='media-meta pull-right'>Popularity: " + this.fields.popularity + strinfo + "</span>"+
                                    "<h4 class='title title-nopad'>"+
                                        "<a onclick=\"recommendTrack(" + "\'" + String(this.fields.uri) + "\'" + ")\" href='#'>"+
                                            this.fields.track +
                                        '</a>'+
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

        if (search.length == 0){
            $("#observe-list").append(

                "<tr class='searchres'>"+
                    "<td>"+
                        "<div class='row media addpad20'>"+
                            "<div class='col-md-11'>"+
                                "<div class='media-body'>"+
                                    "<p class='summary'>Nothing found :(</p>"+
                                "</div>"+
                            "</div>"+
                        "</div>"+
                    "</td>"+
                "</tr>"
            );
        }

    }
    if (itemSelectType == "Location"){

        // Adds each new message item to the list
        $(htracks).each(function() {

            $("#observe-list").append(

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
                                        "<span class='media-meta pull-right'>Popularity: " + this.fields.popularity + " - Hits: " + this.fields.duplicates + "</span>"+
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

        if (htracks.length == 0){
            $("#observe-list").append(

                "<tr class='searchres'>"+
                    "<td>"+
                        "<div class='row media addpad20'>"+
                            "<div class='col-md-11'>"+
                                "<div class='media-body'>"+
                                    "<p class='summary'>Nothing found :(</p>"+
                                "</div>"+
                            "</div>"+
                        "</div>"+
                    "</td>"+
                "</tr>"
            );
        }

    }
    else{

    }

    if(search.length == 0 & artists.length == 0 & genres.length == 0 & playlists.length == 0){

    }


    // Scroll to the top of the scroll-window
    var objDiv = document.getElementById("scroll-window-observe");

    if (objDiv != null){
        objDiv.scrollTop = 0;
    }
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
                                        "<a class = 'playlistscript' onclick=\"GetPlaylist(" + "\'" + String(this.fields.uri) + "\'" +", " +"\'" + String(this.fields.ownerid) + "\'" + ")\" href='#'>"+
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
    if(search.length == 0 & artists.length == 0 & genres.length == 0 & playlists.length == 0){
        $("#explore-list").append(

            "<tr class='searchres'>"+
                "<td>"+
                    "<div class='row media addpad20'>"+
                        "<div class='col-md-11'>"+
                            "<div class='media-body'>"+
                                "<p class='summary'>Nothing found :(</p>"+
                            "</div>"+
                        "</div>"+
                    "</div>"+
                "</td>"+
            "</tr>"
        );
    }

    checkIfLoggedIn(listdata);

    // Scroll to the top of the scroll-window
    var objDiv = document.getElementById("scroll-window-explore");

    if (objDiv != null){
        objDiv.scrollTop = 0;
    }

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
    getYou();

    if(document.getElementById("item")){
        document.getElementById("item")
            .addEventListener("keyup", function(event) {
            event.preventDefault();
            if (event.keyCode == 13) {
                document.getElementById("item").click();
            }
        });
    }

    var elementExists = document.getElementById("settings");
    if (elementExists){
        window.setInterval(getYou, 2000);
    }


// causes list to be re-fetched every 5 seconds
// window.setInterval(getList, 5000);
});
