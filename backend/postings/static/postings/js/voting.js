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

function registerEvents () {
	$(document.body)
	.off('click.js_vote_up')
	.on('click.js_vote_up',
		'.js_vote_up',
		function (event) {
			event.preventDefault();
			console.log("updoot");
		});

	$(document.body)
		.off('click.js_vote_down')
		.on('click.js_vote_down',
			'.js_vote_down',
			function (event) {
				event.preventDefault();
				console.log("downdoot");
			});
}

registerEvents();
