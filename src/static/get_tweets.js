
function fetchNewTweets(keyword, page) {
  $.getJSON('/tos/tweets/'+keyword, function(data) {
    tweetHtml = [];
    $.each(data.tweets, function(i, tweet) {
      tweetHtml.push('<li><span>'+tweet.text+'</span><div class="author">'
                     +'<a href=http://twitter.com/#!/'+tweet.user_name
                     +'>@'+tweet.user_name+'</a></div></li>\n');
    });
    $('#tweets_list').html(tweetHtml.join(''));
    $('#proportion').html('Matched '+data.proportion[0]+' tweets out of '
                          + data.proportion[1] + ' total tweets');
  });
}
