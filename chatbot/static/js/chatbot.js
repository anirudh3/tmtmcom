// Sends a new request to update the to-do list
function getList() {
    $.ajax({
        url: "/socialnetwork/get-list-json",
        dataType : "json",
        success: updateList
    });
}

function getCSRFToken() {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
        if (cookies[i].startsWith("csrftoken=")) {
            return cookies[i].substring("csrftoken=".length, cookies[i].length);
        }
    }
    return "unknown";
}

function updateList(listdata) {
    posts = jQuery.parseJSON(listdata["item"])
    comments = jQuery.parseJSON(listdata["comment"])
    posters = jQuery.parseJSON(listdata["poster"])

    // Make an array of usernames
    var user_list = {};
    var comm_html = {}

    $(posters).each(function() {
        var namething = this.fields.name
        user_list[this.fields.username] = namething;
    });
    // Removes the old to-do list items
    $(".postitem").remove();

    // Adds each new todo-list item to the list
    $(posts).each(function() {
        
        var post_name = user_list[this.fields.user]
        var filt_comm = comments
        var post_id = this.pk

        // Make sure the comment is actually relevant to the post
        $(filt_comm).each(function(){
            var post_num = this.fields.item 
            var comm_name = user_list[this.fields.user]
            if (post_num == post_id){
                var temp_html = (
                        '<div class="jumbotron col-md-12">'+
                            '<span class="details">'+
                                '<div class="row">'+
                                    '<form action="/socialnetwork/profile/'+ comm_name +'/" method="GET" class="form-inline">'+
                                       '<input type="submit" value="'+ comm_name +'" class="btn btn-link col-xs-11" style="vertical-align: middle">'+
                                       '<p style="padding-top: 15px">commented on '+ Date(this.fields.created) +'</p>'+
                                   '</form>'+
                                    '<form class="form-inline" action="">'+
                                        '<div>'+
                                            '<input type="submit" onclick="AddFollow(\''+ comm_name +'\')" value="Follow!" class="btn btn-link col-xs-11" style="vertical-align: middle">'+
                                        '</div>'+
                                    '</form>'+
                                '</div>'+
                            '</span>'+
                        '<p class="lead" style="word-wrap: break-word">'+ this.fields.text +'</p>'+
                        '</div>'
                    )

                if(comm_html[post_id] == undefined){
                    comm_html[post_id] = temp_html
                }
                else{
                    comm_html[post_id] = comm_html[post_id] + temp_html
                }
            }
            else{
                delete this
            }
        });


        // Come up with comment HTML in text form
        $(filt_comm).each(function(){
            var comm_name = user_list[this.fields.user]

            });

        // If there are no comments, set comm_html for that post-id to a space
        if(comm_html[post_id] == undefined){comm_html[post_id] = " "} 

        
        $("#post-feed").append(
            
            "<div class='jumbotron col-lg-12 postitem'>"+
                "<span class='details'>"+
                    "<div class='row'>"+
                        '<form action="/socialnetwork/profile/'+ post_name +'/" method="GET" class="form-inline">'+

                            "<input type='submit' value="+ post_name +" class='btn btn-link col-xs-11' style='vertical-align: middle'>"+
                                
                            "<p style='padding-top: 15px'>posted on "+ Date(this.fields.created) +"</p>"+

                        '</form>'+
                        '<form class="form-inline" action="">'+
                            '<div>'+
                                '<input type="submit" onclick="AddFollow(\''+post_name+'\')" value="Follow!" class="btn btn-link col-xs-11" style="vertical-align: middle">'+
                                '<input type="submit" onclick="UnFollow(\''+post_name+'\')" value="Unfollow..." class="btn btn-link col-xs-11" style="vertical-align: middle">'+
                            '</div>'+
                        '</form>'+
                    '</div>'+
                '</span>'+
                '<p class="lead" style="word-wrap: break-word">'+this.fields.text+'</p>'+

                '<form class="add-form" action="">'+
                    '<div class="input-group input-group-lg">'+
                        '<input placeholder="Comments" class="form-control my-0" aria-describedby="sizing-addon1" id="commentbox" name="commentbox">'+
                    '</div>'+
                    '<div class="col-xs-12" style="height:10px;"></div>'+
                    '<div class="input-group input-group-lg">'+
                        '<input class="btn btn-outline-primary" type="submit" text="Add comment" onclick="AddComment(\''+ post_id +'\')">'+
                    '</div>'+
                '</form>'+

                comm_html[post_id]+     
            '</div>'

        );
    });
}


function sanitize(s) {
    // Be sure to replace ampersand first
    return s.replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;');
}

function displayError(message) {
    $("#error").html(message);
}

function getCSRFToken() {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
        if (cookies[i].startsWith("csrftoken=")) {
            return cookies[i].substring("csrftoken=".length, cookies[i].length);
        }
    }
    return "unknown";
}

function AddFollow(id) {
    console.log("AddFollow was run")
    $.ajax({
        url: "/socialnetwork/follow/"+id+"/",
        type: "POST",
        data: "&csrfmiddlewaretoken="+getCSRFToken(),
        dataType : "json",
        success: updateList
    });
}

function UnFollow(id) {
    console.log("UnFollow was run")
    $.ajax({
        url: "/socialnetwork/unfollow/"+id+"/",
        type: "POST",
        data: "&csrfmiddlewaretoken="+getCSRFToken(),
        dataType : "json",
        success: updateList
    });
}

function AddComment(post_id){

    console.log("AddComment was run")
    var itemTextElement = $("#commentbox");
    var itemTextValue   = itemTextElement.val();

    // Clear input box and old error message (if any)
    itemTextElement.val('');
    displayError('');

    $.ajax({
        url: "/socialnetwork/add-comment/"+post_id+"/",
        type: "POST",
        data: "item="+itemTextValue+"&csrfmiddlewaretoken="+getCSRFToken(),
        dataType : "json",
        success: function(response) {
            if (Array.isArray(response)) {
                updateList(response);
            } else {
                displayError(response.error);
            }
        }
    });

}

function addItem() {
    var itemTextElement = $("#item");
    var itemTextValue   = itemTextElement.val();

    // Clear input box and old error message (if any)
    itemTextElement.val('');
    displayError('');

    $.ajax({
        url: "/jquery-todolist/add-item",
        type: "POST",
        data: "item="+itemTextValue+"&csrfmiddlewaretoken="+getCSRFToken(),
        dataType : "json",
        success: function(response) {
            if (Array.isArray(response)) {
                updateList(response);
            } else {
                displayError(response.error);
            }
        }
    });
}

function deleteItem(id) {
    $.ajax({
        url: "/jquery-todolist/delete-item/"+id,
        type: "POST",
        data: "csrfmiddlewaretoken="+getCSRFToken(),
        dataType : "json",
        success: updateList
    });
}

// The index.html does not load the list, so we call getList()
// as soon as page is finished loading
window.onload = getList;

// causes list to be re-fetched every 5 seconds
window.setInterval(getList, 5000);



