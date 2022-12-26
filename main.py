import multiprocessing as mp
import requests
import json
import time
import datetime


# Get the current date
today = datetime.date.today()

# Get the date two days ago by subtracting a timedelta from the current date
two_days_ago = today - datetime.timedelta(days=2)

# Format the date as a string in the desired format
date_string = two_days_ago.strftime('%Y-%m-%d')


#------------------ actual code---------------------------------

#input variables for the class
token1 = 'AAAAAAAAAAAAAAAAAAAAAI1thwEAAAAAZcmgBw%2FIyiEHTutSe9h943W64DU%3DVbW200bFAVCDNS4u7xFDjBsCiRc0FT8QAUUWAxwIfU6Bl7hDzk'
token2='AAAAAAAAAAAAAAAAAAAAAFOSkgEAAAAAuWgPALsN1RBd%2BTH89wA8bRpRm4c%3Dk3BycFNCxSoBxRxp1nk0YTCl73IWsZEL1mM78TeXK7yS8UVDf3'
token3='AAAAAAAAAAAAAAAAAAAAAJSSkgEAAAAAslQRvg5pQT5i4g6n8pJ6pmvv8mg%3DYXnwlyyvM6BMNfJUqH2jxsK2JIcHJMnG0AIVFigIm8Lfs3BsyQ'
token4='AAAAAAAAAAAAAAAAAAAAAMKSkgEAAAAAYt9v8XhDEZ2a9i9LUPR6bljlQ9g%3DODwTwgpoLVHv4pRRTvszw1XXB4RrocjjmD89PdQBJ8VlCxUsii'

tweet_fields= "created_at,public_metrics,author_id"
#queryies
start_time = f'{date_string}T12:00:01.000Z'
#queryList = ['CVE-2022-42821','CVE-2022-37958','CVE-2022-41082','CVE-2022-41080','CVE-2022-41040','CVE-2021-28655','CVE-2021-33621','CVE-2022-42475','CVE-2022-42710','CVE-2022-46689']
queryList=['bagina','penis','coochie','dookie','innards','twerk','douche','poop','drag','corn dog']
queryList1 =queryList[:1]
queryList2=queryList[2:4]
queryList3=queryList[5:7]
queryList4=queryList[8:10]

final_CVE={}


def getfollower(ID,token):
    header = {'Authorization': f"Bearer {token}"}
    params = {'user.fields': 'public_metrics', }
    print('*****************************Getting User followers*****************************')
    result = requests.get(f'https://api.twitter.com/2/users/{ID}', params=params, headers=header)
    # print(result.json())
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
                'max_results':'80',
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
                followers.append(getfollower(i,self.token))
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
            print('-----------------5 second break before next operation-----------------')
            time.sleep(5)


#initialize the class
searchBot1 = TwitterClient(token1)
searchBot2= TwitterClient(token2)
searchBot3= TwitterClient(token3)
searchBot4=TwitterClient(token4)
#activate query
try:
    searchBot1.search_function(queryList1,tweet_fields,start_time)
except:
    print('Censored/No Results')
try:
    searchBot2.search_function(queryList2,tweet_fields,start_time)
except:
    print('Censored/No Results')
try:
    searchBot3.search_function(queryList3,tweet_fields,start_time)
except:
    print('Censored/No Results')
try:
    searchBot4.search_function(queryList4,tweet_fields,start_time)
except:
    print('Censored/No Results')
print(sorted(final_CVE.items(), key=lambda x:x[1], reverse=True))
