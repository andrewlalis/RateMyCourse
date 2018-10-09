$(function() {
	function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

	$(".vote-up").click(function() {
		var reviewId = $(this).attr("data-review-id");
		// Vote up
	});
	$(".vote-down").click(function() {
		var review = $(this).attr("data-review-id");
		// Vote down
	});
});