var $ = jQuery;

// Load the handlebars template and use it to append all reviews.
function displayReviews(reviews) {
	var template = Handlebars.compile($("#review_item_handlebars").html());
	var container = $("#review_container");
	reviews.forEach(function (review) {
		var review_html = template(review);
		container.append(review_html);
		// If a rating is defined, then hide only those rating stars which are higher than the current rating.
		// TODO: remove this check once this is added to the database.
		if (typeof(review.rating) !== "undefined") {
			$(".js_review_rating").each(function (index) {
				if ((index + 1) > review.rating) {
					this.hide();
				}
			});
		}
		container.append("<hr><br />");
	});
}

function loadReviews () {
	$.ajax({
		url: "http://localhost:8000/api/postings/",
		method: "GET"
	}).done(function (response) {
		displayReviews(response);
	}).fail(function (response) {
		console.log("Could not get postings.");
	})
}

loadReviews();