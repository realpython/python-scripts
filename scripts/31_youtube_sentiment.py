import sys
import requests
from bs4 import BeautifulSoup as bs4

"""
Example usage:

$ python 31_youtube_sentiment.py https://www.youtube.com/watch?v=_vrAjAHhUsA
"""


def get_arguments():
    if len(sys.argv) is 2:
        return sys.argv[1]
    else:
        print('Specify at least 1 argument')
        sys.exit()


def get_comments(url):
    html = requests.get('https://plus.googleapis.com/u/0/_/widget/render/comments?first_party_property=YOUTUBE&href=' + url)
    soup = bs4(html.text, 'html.parser')
    return [comment.string for comment in soup.findAll('div', class_='Ct')]


def calculate_sentiment(comments):
    positive = 0
    negative = 0
    negative_words = [
        'hate', 'hated', 'dislike', 'disliked', 'awful', 'terrible', 'bad',
        'painful', 'worst', 'suck', 'rubbish', 'sad', 'sodding'
    ]
    positive_words = [
        'love', 'loved', 'like', 'liked', 'awesome', 'amazing', 'good',
        'great', 'excellent', 'brilliant', 'cool'
    ]
    for comment in comments:
        if comment is None:
            continue
        else:
            for word in comment.split(' '):
                if word in negative_words:
                    negative += 1
                if word in positive_words:
                    positive += 1
    return {'positive': positive, 'negative': negative}


def main():
    url = get_arguments()
    if url:
        comments = get_comments(url)
        if len(comments) <= 0:
            print('This video has no comments.')
            sys.exit()
        sentiment = calculate_sentiment(comments)
        positive_score = sentiment['positive']
        negative_score = sentiment['negative']
        total_score = positive_score + negative_score
        if positive_score > negative_score:
            print('This video is generally positive:')
            print('{0} positive / {1} total hits'.format(
                positive_score, total_score))
        elif negative_score > positive_score:
            print('This video is generally negative:')
            print ('{0} negative / {1} total hits'.format(
                negative_score, total_score))
        else:
            print('This video is mutual:')
            print('{0} positive {1} negative'.format(
                positive_score, negative_score))
    else:
        print('No url supplied')


if __name__ == '__main__':
    main()
