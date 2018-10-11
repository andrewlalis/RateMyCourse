// $(function() {
//     var csrftoken = $("#csrf-token input").val();

// 	$(".vote-up").click(function() {
// 		var reviewId = $(this).attr("data-review-id");
// 		var data = {
// 			'csrfmiddlewaretoken': csrftoken,
// 			'helpful': true
// 		};
// 		// Vote up
// 		$.post(
// 			'/api/postings/reviews/' + reviewId + '/helpful_vote/',
// 			data,
// 			function(result) { console.log(result); }
// 		);
// 		// Hide vote buttons
// 		$("#review-votes-" + reviewId + " .review-vote-buttons").hide();
// 	});
// 	$(".vote-down").click(function() {
// 		var reviewId = $(this).attr("data-review-id");
// 		var data = {
// 			'csrfmiddlewaretoken': csrftoken,
// 			'helpful': false
// 		};
// 		// Vote down
// 		$.post(
// 			'/api/postings/reviews/' + reviewId + '/helpful_vote/',
// 			data,
// 			function(result) { console.log(result); }
// 		);
// 		// Hide vote buttons
// 		$("#review-votes-" + reviewId + " .review-vote-buttons").hide();
// 	});
// });

// Sends either an up- or down-vote for a particular review.
function sendVote (event, is_helpful) {
	var csrf_token = $('#csrf-token input').val();
	var review_id = $(event.target).closest('.js_votes').data('review_id');
	var data = {
		'csrfmiddlewaretoken': csrf_token,
		'helpful': is_helpful
	};
	$.post(
		'/api/postings/reviews/' + review_id + '/helpful_vote/',
		data,
	)
		.done(function (response) {
			console.log(response);
		})
		.fail(function (response) {
			console.log(response);
		});
}

// Registers all events to the document.
function registerEvents () {
	$(document.body)
	.off('click.js_vote_up')
	.on('click.js_vote_up',
		'.js_vote_up',
		function (event) {
			event.preventDefault();
			console.log("updoot");
			sendVote(event, true);
		});

	$(document.body)
		.off('click.js_vote_down')
		.on('click.js_vote_down',
			'.js_vote_down',
			function (event) {
				event.preventDefault();
				console.log("downdoot");
				sendVote(event, false);
			});
}

registerEvents();
