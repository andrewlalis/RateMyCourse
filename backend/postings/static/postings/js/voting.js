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
			var selector = '#votes_';
			if (is_helpful) {
				selector += 'helpful_';
			} else {
				selector += 'unhelpful_';
			}
			var $vote_display = $(selector + review_id);

			var current_votes = parseInt($vote_display.html());
			$vote_display.html(current_votes + 1);

			$('#review-votes-' + review_id + ' .review-vote-buttons').hide();
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
