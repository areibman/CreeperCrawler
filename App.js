var comments = [];
var userID = [];
var picURL = [];
var friendURL = [];
var friendPicture = [];
var friendName = [];
var groupName = [];
var groupURL = [];
var likes = [];


var page = 'https://facebook.com/siyangqiu';
var id = 'me';
var key = 'access_token=EAACEdEose0cBACpqjddo3RY8AeLhZCqOD1MZBy5sZAch9PEZC2hZCtbXVa2ol0G69oNOJKmQ3cP1mSdNxbnZBbYkFymjGzRyNclE0qHCCPK3psuZAOLZB4cyrjyRHvZCefeLV6wI0r7O8A3rUSY0NBbYlp92X8bJB0VAVmQicydZCJLC97sFNAfFEZBk6bPH7VCaCqZC3Oo8xPUNZBwZDZD';

var graphAPI = 'https://graph.facebook.com/' + id;

var getComments = function(uri) {
	var allUserPosts;
	var individualPost = [];
	$.getJSON(uri, function( data ) {
		allUserPosts = data.data;
		for (i = 0; i < allUserPosts.length; i++) {
			if (allUserPosts[i].comments != null) {
				individualPost.push(allUserPosts[i].comments.data);
			}
		}
		for (i = 0; i < individualPost.length; i++) {
			for (j = 0; j < individualPost[i].length; j++) {
				comments.push(individualPost[i][j].message);
				userID.push(individualPost[i][j].from.id);
			}
		}
		$( "<h3/>", {
		"id": 'comments',
		html: 'User ID of Commentors'
		}).appendTo( "body" );
		pushTable(userID,'userID');
		pushTable(comments,'comments');
	});

}
var getPics = function(uri) {
	var picData;
	$.getJSON(uri, function( data ) {
		picData = data.data;
		for (i = 0; i < picData.length; i++) {
			if (picData[i].link != null) {
				picURL.push(picData[i].link);
			}
		}
		$( "<h3/>", {
		"id": 'pictures',
		html: 'URLs of Photos Uploaded'
		}).appendTo( "body" );
		pushTable(picURL,'picURL');
	});	
	
}
var getLikes = function(uri) {
	var picData;
	$.getJSON(uri, function( data ) {
		picData = data.data;
		for (i = 0; i < picData.length; i++) {
			likes.push(picData[i].name);
		}
		console.log(likes);
		$( "<h3/>", {
		"id": 'likes',
		html: 'Pages Users Liked'
		}).appendTo( "body" );
		pushTable(likes,'likes');
	});	
}

var getFriends = function(uri) { 
	$.getJSON(uri, function( data ) {
		$.each(data, function(key,value){
			friendName.push(value.name);
			friendPicture.push(value.image);
			friendURL.push(value.profile);
		});
		$( "<h3/>", {
		"id": 'friends',
		html: 'List of Friends (Name, picture, url)'
		}).appendTo( "body" );
		pushTable(friendName,'friendName');

		var items = [];
		for (i= 0; i< friendPicture.length; i++){
			items.push( '<td><img src="' + friendPicture[i] + '"</td>' );
		}
		$( "<tr/>", {
		"id": 'friendPicture',
		html: items.join( "" )
		}).appendTo( "body" );
		pushTable(friendURL,'friendURL');
	});	
}

var getGroups = function(uri) { 
	$.getJSON(uri, function( data ) {
		$.each(data, function(key,value){
			groupName.push(value);
			groupURL.push('http://facebook.com'+key);
		});
		$( "<h3/>", {
		"id": 'groups',
		html: 'List of Groups the User Joined'
		}).appendTo( "body" );
		pushTable(groupName,'groupName');
		pushTable(groupURL,'groupURL');
	});	
}

var pushTable = function(data,name) {
	var items = [];
	for (i= 0; i< data.length; i++){
		items.push( "<td>" + data[i] + "</td>" );
	}
		$( "<tr/>", {
		"id": name,
		html: items.join( "" )
		}).appendTo( "body" );
}


$(document).ready(function(){
	getFriends('friends.json');
	getGroups('groups.json');
	getComments(graphAPI + '/posts?fields=comments&' + key);
	getPics(graphAPI + '/photos?fields=link&' + key);
	getLikes(graphAPI + '/likes?' + key);
//	
});












//FB SDK
window.fbAsyncInit = function() {
FB.init({
  appId            : '273072363231556',
  autoLogAppEvents : true,
  xfbml            : true,
  version          : 'v2.12'
});
};

(function(d, s, id){
 var js, fjs = d.getElementsByTagName(s)[0];
 if (d.getElementById(id)) {return;}
 js = d.createElement(s); js.id = id;
 js.src = "https://connect.facebook.net/en_US/sdk.js";
 fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));
