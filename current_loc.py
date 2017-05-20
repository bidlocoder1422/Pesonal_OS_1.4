import requests
import json


class location:
    """returns current loc dict or city
        or 1 if connection is down
    """

    def return_city():
        send_url = 'http://freegeoip.net/json'
        try:
            answer = requests.get(send_url)
            sort = json.loads(answer.text)
        except Exception:
            return 'Unavailable'
        if not sort.get('city')==' ' :
            return sort.get('city')
        else: return ('Unavailable')

    def return_coord():
        send_url = 'http://freegeoip.net/json'
        try:
            answer = requests.get(send_url)
            sort = json.loads(answer.text)
            for i in sort.keys():
                print(i, ' : ',sort.get(i))
            input()
        except Exception:
            print('Unavailable')
