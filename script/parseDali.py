import requests
import json
import sched, time
from datetime import datetime
def getAQX(url):
  retryCnt = 5
  r = requests.get(url)
  while retryCnt >0:
      r = requests.get(url)
      if r.status_code == 200:
        return r.text
      print('Retry : {} '.format(retryCnt))
      retryCnt = retryCnt -1
  return False

def exec_request(sc):
  url = 'http://opendata.epa.gov.tw/ws/Data/AQX/?$filter=SiteName%20eq%20%27%E5%A4%A7%E9%87%8C%27&$orderby=SiteName&$skip=0&$top=1000&format=json'
  data = getAQX(url)
  if data:
    with open('../json/dali.json', 'w') as f:
      json.dump(data, f)
    print ("{}| parse DONE".format(datetime.now()))
  else:
    print ("{} parse ERROR".format(datetime.now()))
  sc.enter(60*30, 0, exec_request, (sc,)) # crawl while 1 hour
if __name__ == '__main__':
  s = sched.scheduler(time.time, time.sleep)
  s.enter(0, 0, exec_request, (s,))
  s.run()
