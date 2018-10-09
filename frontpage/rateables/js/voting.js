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
			'/api/postings/reviews/' + reviewId + '/helpful_vote',
			data
		);
	});
	$(".vote-down").click(function() {
		var review = $(this).attr("data-review-id");
		var data = {
			'csrfmiddlewaretoken': csrftoken,
			'helpful': false
		};
		// Vote down
		$.post(
			'/api/postings/reviews/' + reviewId + '/helpful_vote',
			data
		);
	});
});