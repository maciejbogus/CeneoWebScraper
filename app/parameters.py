selectors = {
    "author" : ["span.user-post__author-name"],
    "recomendation" : ["span.user-post__author-recomendation > em"],
    "stars" : ["span.user-post__score-count"],
    "content" : ["div.user-post__text"],
    "pros" : ["div[class$=\"positives\"]~ div.review-feature__item", None, True],
    "cons" : ['div[class$=\"negatives\"]~ div.review-feature__item', None, True],
    "usefull": ['span[id^="votes-yes"]'],
    "useless": ['span[id^="votes-no"]'],
    "publish_date" : ["span.user-post__published > time:nth-child(1)", "datetime"],
    "purchase_date" : ["span.user-post__published > time:nth-child(2)", "datetime"]
}