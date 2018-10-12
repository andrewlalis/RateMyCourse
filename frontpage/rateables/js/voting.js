$(function() {
    var csrftoken = $("#csrf-token input").val();

	$(".vote-up").click(function() {
		var reviewId = $(this).attr("data-review-id");
		var data = {
			'csrfmiddlewaretoken': csrftoken,
			'helpful': true
		};
		// Vote up
		$.post(
			'/api/postings/reviews/' + reviewId + '/helpful_vote/',
			data,
			function(result) { console.log(result); }
		);
		// Hide vote buttons
		$("#review-votes-" + reviewId + " .review-vote-buttons").hide();
	});
	$(".vote-down").click(function() {
		var reviewId = $(this).attr("data-review-id");
		var data = {
			'csrfmiddlewaretoken': csrftoken,
			'helpful': false
		};
		// Vote down
		$.post(
			'/api/postings/reviews/' + reviewId + '/helpful_vote/',
			data,
			function(result) { console.log(result); }
		);
		// Hide vote buttons
		$("#review-votes-" + reviewId + " .review-vote-buttons").hide();
	});
});