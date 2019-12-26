import tweepy

auth = tweepy.OAuthHandler('q2Chl7HHOTmUvuvoOYzgjmMnF', 'BkTNT9qS0MLSosdyMN4ySf51BI3yaG1ifYjLXhb7XBsFvHtaXw')
auth.set_access_token('92157944-KXb4WLrLnMN0NnzcYLSR8jVMjH8nW8OUcBiSdH6cF', 'PuqWG5x6VGwIIBhHrO5jsK66ov2s9YMxxvVCwfllgGvyY')

api = tweepy.API(auth, wait_on_rate_limit=True)
