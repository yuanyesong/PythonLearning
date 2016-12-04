import http.client
conn = http.client.HTTPConnection("www.badu.com")
conn.request("HEAD","/")
res = conn.getresponse()
conn.close()
print(res.status,res.reason)
