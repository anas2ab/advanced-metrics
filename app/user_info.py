import private

my_api = private.api
tweep = private.tweepy

def get_difference_in_followers(account):
    user = my_api.get_user(account)


   
    followers_list = my_api.followers_ids(user.screen_name, -1)
    following_list = my_api.friends_ids(user.screen_name,-1)

    

    not_followers_list = list(set(following_list) - set(followers_list))
    
    return not_followers_list




