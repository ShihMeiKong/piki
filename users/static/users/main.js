var login = function(event){
	event.preventDefault()
	console.log("In js login")
	window.location.href = '/users/login';
}

var profile = function(event){
	event.preventDefault()
	console.log("In js profile")
	window.location.href = '/users/profile';
	// $.ajax({
	// 	type:"GET",
	// 	url: "/users/profile",
	// }).then(function(resp) {
	// 	console.log("Response", resp)
	// })
}
// storing the checkbox state in the user's computer using local storage
// getItem modifies localStorage in JS
// using key/value pairs for checkbox id and if the checkbox is checked or not
// but since local storage can only handle key/value pairs, need to stringify the object before storing and on retrieval
// var checkboxValues = JSON.parse(localStorage.getItem('checkboxValues');
// 	if (checkboxValues === null){
// 		checkboxValues= {};
// var $checkbox = $('#checkbox-useris :checkbox');

// $checkbox.on("change", function(){
// 	$checkbox.each(function(){
// 		checkboxValues[this.id] = this.checked;
// 	});
// 	localStorage.setItem("checkboxValues", JSON.stringify(checkboxValues));
// });
// // iterate over the checkboxValues when teh page loads
// $.each(checkboxValues, function(key, value){
// 	$("#" + key).prop('checked', value);
// });

var logout = function(event){
	event.preventDefault()
	console.log("In js logout")
	window.location.href = '/users/logout';
	// $.ajax({
	// 	type:"POST",
	// 	url: "/users/logout",
	// })
}

// var userPref = function(event){
// 	event.preventDefault()
// 	console.log("In saving userpref")
// 	$.ajax({
// 		type:"POST",
// 		url: "/users/userprefsubmit",
// 	})
// }

$(document).ready(function(){
	console.log("Page loaded")
	// $('#checkbox-useris :checkbox').on("change", function(){
	// 	alert("You have changed your preferences");
	// });
	$('.logoutbutton').on('click', logout);
	// $('.userprefsubmit').on('submit', userPref);
	$('.profilebutton').on('click', profile);
	$('.loginbutton').on('click', login);

})