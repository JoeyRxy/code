import requests

if __name__ == "__main__":
    url = "https://movie.douban.com/top250"
    # url = "http://maoyan.com/board/"
    # url = "http://www.google.com"
    requests.packages.urllib3.disable_warnings()
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.text)
    # print("hello world")
