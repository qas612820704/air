import requests
import json
import sched, time
from datetime import datetime
def getAQX(url):
  retryCnt = 0
  while retryCnt < 6:
    try:
      r = requests.get(url,timeout=5)
      if r.status_code == 200:
        return r.text
      retryCnt = retryCnt + 1
      print('Retry : {} '.format(retryCnt))
    except Exception as e:
      print (e)
  return False

def exec_request(sc):
  url = 'http://opendata.epa.gov.tw/ws/Data/AQX/?$orderby=SiteName&$skip=0&$top=1000&format=json' 
  data = getAQX(url)
  if data:
    data = data.__str__().replace('PM2.5','PM2p5')
    with open('../json/all.json', 'w') as f:
      f.write(data)
    print ("{}| parse DONE".format(datetime.now()))
  else:
    print ("{} parse ERROR".format(datetime.now()))
  sc.enter(60*30, 0, exec_request, (sc,)) # crawl while 1 hour
if __name__ == '__main__':
  s = sched.scheduler(time.time, time.sleep)
  s.enter(0, 0, exec_request, (s,))
  s.run()
