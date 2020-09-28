import requests
import re
from bs4 import BeautifulSoup

res = requests.get("http://www.chandrashekar.info/user/login")
if res.status_code != 200:
    print("Failed to initiate login: ", res.status_code)

cookies = res.cookies
html = BeautifulSoup(res.text, "html")
form_build_id = html.select("input[name='form_build_id']")[0]["value"]

#form_build_id = re.search(r'\"form_build_id\"\s+value\s*=\s*\"(.+?)"',
#                    res.text).group(1)

print(form_build_id)

form_data = {
    "name"          : "testuser",
    "pass"          : "w3lc0me",
    "form_build_id" : form_build_id,
    "form_id"       : "user_login",
    "op"            : "Log in"
}


res = requests.post("http://www.chandrashekar.info/user/login", data=form_data)
if res.status_code != 200:
    print("Failed during login: ", res.status_code)

print(res.url)

res = requests.get("http://www.chandrashekar.info/node/add/blog", cookies=res.cookies)
if res.status_code != 200:
    print("Failed to fetch blog form: ", res.status_code)



#match = re.search(r'\"form_build_id\"\s+value\s*=\s*\"(.+?)\".+?\"form_token\"\s+value\s*=\s*\"(.+?)\"',
#          res.text, re.S)
#form_build_id, form_token = match.group(1), match.group(2)

html = BeautifulSoup(res.text, "html")
form_build_id = html.select("input[name='form_build_id']")[0]["value"]
form_token = html.select("input[name='form_token']")[0]["value"]

form_data = {
    "title"                 :  "Hello world",
    "body[und][0][value]"   :  "this is a blog message!",
    "body[und][0][summary]" :  "",
    "body[und][0][format]"  :  "filtered_html",
    "changed"               :  "",
    "form_build_id"         :  form_build_id,
    "form_token"            :  form_token,
    "form_id"               :  "blog_node_form",
    "additional_settings__active_tab" : "",
    "op"                    : "Save"
}


res = requests.post("http://www.chandrashekar.info/node/add/blog", data=form_data,
                   cookies=res.cookies)
if res.status_code != 200:
    print("Failed during login: ", res.status_code)

print(res.url)




