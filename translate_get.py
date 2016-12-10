import json
import requests

"""
**set your access token**
1.sinup Google cloud pratform.(GCP)
1.install google cloud sdk and setup it,
2.get service-account key file from GCP (it's maybe json file)
3.type command "gcloud auth activate-service-account --key-file=XXXXXXXXXXXXX.json"
4.type command "gcloud auth print-access-token"
5.token show display .  copy it and set this file and run.

more detail:
https://cloud.google.com/translate/docs/premium
"""
token = '**remove me**' # set token here

#REST api / "premium translation" url not euqal "normal transration" url !
url = "https://translation.googleapis.com/language/translate/v2"
#oldurl = "https://www.googleapis.com/language/translate/v2"

# translate / en -> ja
source = "en"
target = "ja"

# new translation needed
model = "nmt"

# translate target chars / must be less than 2K characters.
# see : https://cloud.google.com/translate/docs/translating-text#translate-translate-text-python
# this is sample chars from : http://web-tan.forum.impressrd.jp/e/2016/11/17/24396
q = "Machine translation is by no means solved. GNMT can still make significant errors that a human translator would never make, like dropping words and mistranslating proper names or rare terms, and translating sentences in isolation rather than considering the context of the paragraph or page. There is still a lot of work we can do to serve our users better. However, GNMT represents a significant milestone. We would like to celebrate it with the many researchers and engineers—both within Google and the wider community—who have contributed to this direction of research in the past few years." # 長いので省略してます

payload = {
    'target':target,
    'source':source,
    'q':q,
    'model':model
}

headers = {
    'Content-Type':'application/json',
    'Authorization': 'Bearer ' + token,
}

response = requests.get(url,params=payload,headers=headers)

# JSON decode
jObj = json.loads(response.text)

print(jObj)
