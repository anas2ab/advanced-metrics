from InstagramAPI import InstagramAPI
import time
import os 

""" username = 'anasboot'
password = 'soccer1BUTT' 



api = InstagramAPI(username,password)
api.login()
time.sleep(2) """
def createAPI(username, password):
    return InstagramAPI(username, password, False, os.path.dirname(os.path.abspath(__file__)))

def getTotalFollowing(api, user_id):
    following = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''
        _ = api.getUserFollowings(user_id, maxid=next_max_id)
        following.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')       

        return following

def getTotalFollowers(api, user_id):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """

    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers



def getNotFollowing(api, user_id):

    # List of all followers
    followers = getTotalFollowers(api, user_id)

    following_list = []
    followers_list = []

    following = getTotalFollowing(api, user_id)


    for user in followers:
        followers_list.append(user['username'])

    for user in following:
        following_list.append(user['username'])

    not_followers_list = list(set(following_list) - set(followers_list))

    return not_followers_list


