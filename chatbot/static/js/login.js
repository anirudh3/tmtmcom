// var spAccessToken

// // Createing Cross Site Reference Forgery tokens
// function getCSRFToken() {
//     var cookies = document.cookie.split(";");
//     for (var i = 0; i < cookies.length; i++) {
//         if (cookies[i].startsWith("csrftoken=")) {
//             return cookies[i].substring("csrftoken=".length, cookies[i].length);
//         }
//     }
//     return "unknown";
// }


// function subForm() {
//     $("#logForm").submit();
// }

// // Function for logging in to spotify
// function SpotifyLogin(){
//     var SPOTIPY_CLIENT_ID = "ba6790bdcd434f06b7b577e344c6e0ae"
//     var SPOTIPY_REDIRECT_URI = "http://localhost:8000/chatbot/callback"
//     var spotifyScope = "playlist-read-private"
//     var state = "GZ2TPEFHXMB4"
//     var spotifyAuthEndpoint = "https://accounts.spotify.com/authorize?"+"client_id="+SPOTIPY_CLIENT_ID+"&redirect_uri="+SPOTIPY_REDIRECT_URI+"&scope="+spotifyScope+"&response_type=token&state="+state;
//     window.open(spotifyAuthEndpoint,'callBackWindow','height=500,width=400');
//     //This event listener will trigger once your callback page adds the token to localStorage
//     window.addEventListener("storage",function(event){
//         if (event.key == "accessToken"){
//             spAccessToken = event.newValue;
//             //do things with spotify API using your access token here!!
//             console.log("call spottoken");
//             // CallSpotToken(spAccessToken);
//             var CrossToken = {
//                 myval: "Yeah!"
//             }
//             subForm();
//             return true;
//         }
//         else{
//             console.log('SpotifyLogin failed')
//             return false;
//         }
//     });
// }

// $(document).ready(function() {
//     $("#logForm").submit(function() {
//         SpotifyLogin();
//         event.preventDefault();

//     });
// });

