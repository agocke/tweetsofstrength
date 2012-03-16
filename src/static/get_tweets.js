
function fetchNewTweets(keyword, page) {
  $.getJSON('/tos/tweets/'+keyword, function(data) {
    tweetHtml = [];
    $.each(data, function(i, tweet) {
      tweetHtml.push('<li><span>'+tweet.text+'</li></span>\n');
    });
    $('#tweets').html(tweetHtml.join(''));
  });
}
