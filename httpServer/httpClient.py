# httpClient for post HttpRequest
#2020年4月23日18:50:34
#xiaobing.sun
#send json Object for Alogithorms
import urllib
import http.client
import utils
import json
import requests

class User:

    def __init__(self):
        print
        'a'

    def login(self, imsi, ua):
        print
        "==============user start login=================="
        input = {
            "method": "user.login",
            "userName": "",
            "userPass": "",
        }

        input["sig"] = utils.getSignature(input)
        params = urllib.urlencode(input)
        headers = {
            "user-agent": ua,
            "Appstore-clientType": "android",
            "Appstore-IMEI": "123456789000000",
            "Appstore-IMSI": imsi
        }

        try:
            connection = httplib.HTTPConnection(utils.API_HOST)
            connection.request("POST", "/api", params, headers)
            response = connection.getresponse().read()
            # print "=========" + response
            connection.close()
        except Exception(e):
            print("========" + str(e))

        if "errorcode" in response or response is None:
            return

        results = json.loads(response)

        return results["results"].encode("utf-8")



url = "http://localhost:8000"
path = "../config/config.json"
print(path)
files = {'file': open(path, 'rb')}
r = requests.post(url, files=files)
print (r.url)
print (r.text)
