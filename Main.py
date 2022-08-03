# I LOVE GURA
# I LOVE GURA
# I LOVE GURA

import requests, re
from pytube import YouTube as yt
from hurry.filesize import size, alternative
from bs4 import BeautifulSoup as bs
from urllib.parse import unquote

author = "Sandy Sayang Gawr Gura"
log = {
    "invalid_url" : {
        "author" : author,
        "status" : 406,
        "message" : "Invalid URL!"
    },
    "exception" : {
        "author" : author,
        "status" : 500,
        "message" : "Whoops! Something wrong!"
    }
}

def TinyURL(url) -> dict:
    """
    URL shortener using TinyURL
    """
    if not re.search(r"http[s]\:\/\/", url):
        return log["invalid_url"]
    try:
        data = requests.get("https://tinyurl.com/api-create.php", params={ "url" : url }).text
        return {
            "author" : author,
            "status" : 200,
            "url" : data
        }
    except:
        return log["exception"]

class YouTube:
    """
    YouTube downloader using Pytube library
    """
    def __init__(self, url) -> None:
        self.url = url
    def audio(self) -> dict:
        if not re.search("youtu.be|youtube.com", self.url):
            return log["invalid_url"]
        try:
            data = yt(self.url)
            raw = data.vid_info
            aa = raw["streamingData"]["adaptiveFormats"]
            res = [a for a in aa if a["itag"] == 140]
            return {
                "author" : author,
                "status" : 200,
                "title" : data.title,
                "description" : data.description,
                "size" : size(data.streams.get_by_itag(140).filesize, system=alternative),
                "thumbnail" : data.thumbnail_url,
                "url" : TinyURL(res[0]["url"])["url"],
                "mimeType" : res[0]["mimeType"]
            }
        except:
            return log["exception"]
    def video(self) -> dict:
        if not re.search("youtu.be|youtube.com", self.url):
            return log["invalid_url"]
        try:
            data = yt(self.url)
            raw = data.vid_info
            aa = raw["streamingData"]["formats"]
            res = [a for a in aa if a["itag"] == 22]
            return {
                "author" : author,
                "status" : 200,
                "title" : data.title,
                "description" : data.description,
                "size" : size(data.streams.get_by_itag(22).filesize, system=alternative),
                "thumbnail" : data.thumbnail_url,
                "url" : TinyURL(res[0]["url"])["url"],
                "mimeType" : res[0]["mimeType"]
            }
        except:
            return log["exception"]
            
def Facebook(url) -> dict:
    """
    Facebook downloader
    """
    if not re.search("www.facebook|m.facebook|fb.watch", url):
        return log["invalid_url"]
    try:
        if re.search("www.facebook", url):
            mbasic = url.replace("www.facebook", "mbasic.facebook")
            data = requests.get(mbasic).text
            html = bs(data, "html.parser")
            a = html.find_all("div", {
                "class" : "ca"
            })
            res = a[0].find("a").get("href")
            return {
                "author" : author,
                "status" : 200,
                "url" : TinyURL(unquote(res.split("src=", 1)[1]))["url"]
                }
        elif re.search("m.facebook", url):
            mbasic = url.replace("m.facebook", "mbasic.facebook")
            data = requests.get(mbasic).text
            html = bs(data, "html.parser")
            a = html.find_all("div", {
                "class" : "ca"
            })
            res = a[0].find("a").get("href")
            return {
                "author" : author,
                "status" : 200,
                "url" : TinyURL(unquote(res.split("src=", 1)[1]))["url"]
                }
        elif re.search("fb.watch", url):
            data = requests.get(url).text
            html = bs(data, "html.parser")
            a = html.find_all("meta", {
                "property" : "og:video:url"
            })
            res = a[0].get("content")
            return {
                "author" : author,
                "status" : 200,
                "url" : TinyURL(unquote(res))["url"]
            }
    except:
        return log["exception"]
        
class Instagram:
    """
    Instagram downloader
    """
    def igtv(url) -> dict:
        if not re.search("instagram.com\/tv\/", url):
            return log["invalid_url"]
        try:
            data = requests.get(url).text
            html = bs(data, "html.parser")
            a = html.find_all("meta", {
                "property" : "og:video"
            })[0]
            res = a.get("content")
            return {
                "author" : author,
                "status" : 200,
                "url" : TinyURL(unquote(res))["url"]
            }
        except:
            return log["exception"]

# I LOVE GURA
# I LOVE GURA
# I LOVE GURA