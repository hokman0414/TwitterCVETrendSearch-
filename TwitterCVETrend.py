 import requests
import json
import time

#input variables for the class
token = 'input token'
tweet_fields= "created_at,public_metrics,author_id"
#queryies
start_time = '2022-10-20T12:00:01.000Z'
queryList = ['CVE-2022-41082','CVE-2022-33882','CVE-2022-42307','CVE-2022-42306','CVE-2022-42305','CVE-2022-42302']

final_CVE={}



def getfollower(ID):
        header={'Authorization':f"Bearer {token}"}
        params={'user.fields':'public_metrics',}
        print('*****************************Getting User followers*****************************')
        result = requests.get(f'https://api.twitter.com/2/users/{ID}', params=params, headers=header)
        #print(result.json())
        followers = result.json()['data']['public_metrics']['followers_count']
        print(f'Author ID:{ID} has {followers} Followers')
        return followers


class TwitterClient:
    def __init__(self,token):
        self.token = token

    def search_function(self,queries,tweet_fields,start_time):
        self.queries = queries
        self.tweet_fields=tweet_fields
        headers = {"Authorization": "Bearer {}".format(self.token)}
        for query in queries:
            url = "https://api.twitter.com/2/tweets/search/recent"
            parameters = {
                'query': query,
                'tweet.fields': tweet_fields,
                'start_time': start_time,
                'max_results':'100',
            }
            response = requests.get(url,params=parameters,headers=headers)
            #print(response.json())


            data=response.json()['data']
            # time it took for the response to get the tweets
            timing = response.elapsed.total_seconds()
            #print(timing, 'seconds')
            print(f'Getting Twitter data from {query}')

            Total_tweets= len(data)
            Total_retweet=[]
            Likes = []
            following=[]
            for i in range(len(data)):
                Total_retweet.append(data[i]['public_metrics']['retweet_count'])
                Likes.append(data[i]['public_metrics']['like_count'])
                following.append(data[i]['author_id'])
            #print(Likes)
            #print(followers)
            #print(Total_retweet)

            #algroithm variables
            retweet_Index = int(sum(Total_retweet))/Total_tweets
            #print(retweet_Index)
            followers=[]
            for i in following:
                followers.append(getfollower(i))
                #time.sleep(10)


            #follower average
            average_followers =int(sum(followers))/Total_tweets
            #print(average_followers)
            Average_likes=[Likes[i]/average_followers for i in range(len(Likes))]
            Average_likes_index=sum(Average_likes)
            P_formula= (Average_likes_index/Total_tweets) + ((average_followers*Total_tweets)/Total_tweets) + retweet_Index + Total_tweets
            print(P_formula/timing, 'score rated')
            final_p=P_formula/timing
            final_CVE.update({query:final_p})
            #take a break before next request
            print('-----------------10 second break before next operation-----------------')
            time.sleep(10)


#initialize the class
searchBot = TwitterClient(token)
#activate query
searchBot.search_function(queryList,tweet_fields,start_time)
print(sorted(final_CVE.items(), key=lambda x:x[1], reverse=True))

