var $ = jQuery;

// Sends POST request to api.
function postReview (data) {
	$.ajax({
		url: "api/postings/",
		method: "POST",
		data: JSON.stringify(data),
		contentType: "application/json",
		headers: {
            'X-CSRFToken': Cookies.get("csrftoken")
        }
	}).done(function (response) {
		var template = Handlebars.compile($("#review_item_handlebars").html());
		var container = $("#review_container");
		var review_html = template(response);
		container.append(review_html);
		container.append("<hr><br />");
	}).fail(function (response) {
		console.log(response);
		alert("The review could not be sent.");
	}).always(function () {
		$("#submit_review_form").trigger("reset");
		$('#close-review-box').trigger("click");
	});
}

// What to do when the user clicks submit.
function onSubmitReviewClicked () {
	var serialized_data = $("#submit_review_form").serializeArray();
	var formatted_data = {};
	for (var i = 0; i < serialized_data.length; i++) {
		formatted_data[serialized_data[i]['name']] = serialized_data[i]['value'];
	}
	console.log(formatted_data);
	postReview(formatted_data);
}

// Add a listener for when the user clicks to submit a review.
$(document.body)
	.off("click.submit_review_button")
	.on("click.submit_review_button",
		"#submit_review_button",
		function (event) {
			event.preventDefault();
			onSubmitReviewClicked();
		});