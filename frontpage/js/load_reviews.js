var $ = jQuery;

Handlebars.registerHelper('times', function(n, block) {
    var accum = '';
    for(var i = 0; i < n; ++i)
        accum += block.fn(i);
    return accum;
});

// Load the handlebars template and use it to append all reviews.
function displayReviews(reviews) {
	var template = Handlebars.compile($("#review_item_handlebars").html());
	var container = $("#review_container");
	container.remove(".review_item");
	reviews.forEach(function (review) {
		var review_html = template(review);
		container.append(review_html);
		container.append("<hr><br />");
	});
}

function loadReviews () {
	$.ajax({
		url: "/api/postings/",
		method: "GET"
	}).done(function (response) {
		displayReviews(response);
	}).fail(function (response) {
		console.log("Could not get postings.");
	})
}

loadReviews();