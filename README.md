# TwitterCVETrendSearch-

project 2:
Have lists of Threat actor names targeting financial industries.
requests all the approved website lists. web scrape data - all the blog infos, mentions of the TA in list
use the partial match function. If values not none (match found at list)- the variable name, + website link to it.



This project mainly interacts with NVD/TWitter API for info.

project 1 - it's like CVE trend but does not reply on audience view count and can search much more vulnerabilites.
function 1. NVD CVE gatherer
2 lists: 1. List_CVE's 2. CVE DICT LIST(CVE:,CVSS metrics, Descriptions)

class Twitter_Client: 
what can it do?(functiions)
1. search_twitter(List_CVE's) return new list with Engagement/popularity calcution
dictionary list
https://blog.hootsuite.com/calculate-engagement-rate/ calculate  with this algorithm.

 generate the csv file w CVSS metrics AV,AC etc

