import http.client
import urllib.parse

def checkUrl(url):
    p = urllib.parse.urlparse(url)
    conn = http.client.HTTPConnection(p.netloc)
    conn.request('HEAD', p.path)
    resp = conn.getresponse()
    return resp.status < 400

if __name__ == '__main__':
    print(checkUrl('http://www.stackoverflow.com')) # True
    print(checkUrl('http://stackoverflow.com/notarealpage.html')) # False