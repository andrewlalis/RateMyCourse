$(function() {
    var csrftoken = $("#csrf-token input").val();

	$(".vote-up").click(function() {
		var reviewId = $(this).attr("data-review-id");
		// Vote up
	});
	$(".vote-down").click(function() {
		var review = $(this).attr("data-review-id");
		// Vote down
	});
});