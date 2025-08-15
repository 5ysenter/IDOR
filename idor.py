import requests

with requests.session() as s:
    for i in range(0, 100):
        response = s.get("http://127.0.0.1/user.php?user=%s" % (str(i)))
        if "admin" in response.text:
            print(response.url)