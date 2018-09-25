var $ = jQuery;

function displayReviews(reviews) {
	
}

function loadReviews () {
	$.ajax({
		url: "http://localhost:8000/api/postings/",
		method: "GET"
	}).done(function (response) {
		displayReviews(response);
	}).fail(function (response) {
		console.log(response);
	})
}

loadReviews();