# TwitterCVETrendSearch-




This project mainly interacts with NVD/TWitter API for info.

project 1 - it's like CVE trend but does not rely on audience view count and can search much more vulnerabilites.
function 1. NVD CVE gatherer
2 lists: 1. List_CVE's 2. CVE DICT LIST(CVE:,CVSS metrics, Descriptions)

class Twitter_Client: 
what can it do?(functiions)
1. search_twitter(List_CVE's) return new list with Engagement/popularity calcution
dictionary list
(https://aparav.github.io/2016/12/26/how-i-built-an-app-from-scratch/) calculate  with this algorithm.

 generate the csv file w CVSS metrics AV,AC etc

![image](https://user-images.githubusercontent.com/106271123/198939951-70598c88-259e-41fa-8879-d01b4088c3d3.png)
special thanks to Aparajithan Venkateswaran for this algorithim.
