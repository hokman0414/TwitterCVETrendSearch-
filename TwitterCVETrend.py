
import requests
import json

#input variables for the class
token = 'ENTER TWITTER BEARER TOKEN'
tweet_fields= "created_at,public_metrics"
#querry
query="CVE-2022-41040 "

start_time = '2022-10-04T12:00:01.000Z'
queryList = ['CVE-2022-41040','CVE-2022-41082','CVE-2022-30190','CVE-2020-6201',
             'CVE-2020-6201','CVE-2022-42247','CVE-2022-33882','CVE-2022-42307','CVE-2022-42306',
             'CVE-2022-42305','CVE-2022-42302']
CVE_Ranking ={}
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
            #print(query)
            #print(response.status_code)
            #engagement per post - hint of popularity
            engagementsScore =sum([response.json()['data'][i]['public_metrics']['retweet_count']+
                                    response.json()['data'][i]['public_metrics']['like_count']+
                                    response.json()['data'][i]['public_metrics']['reply_count']
                                    for i in range(len(response.json()['data']))]) / len(response.json()['data'])
            rank = {query:engagementsScore}
            CVE_Ranking.update(rank)
        #sort
        print(sorted(CVE_Ranking.items(), key=lambda x:x[1], reverse=True))
        return sorted(CVE_Ranking.items(), key=lambda x:x[1], reverse=True)



#initialize the class
searchBot = TwitterClient(token)
#activate query
print(searchBot.search_function(queryList,tweet_fields,start_time))




