import urllib3
import json
from urllib.parse import urlparse, parse_qs, unquote

def lambda_handler(event, c):
    url = event["url"]
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    headers = {}
    if "headers" in query_params:
        headers_str = unquote(query_params["headers"][0])
        # example of what headers_str is: {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Connection": "keep-alive","Cookie": "__cf_bm=VTD.yb16LSAMEU135hG848uASIgj0suVqwH.6F5S2os-1712620754-1.0.1.1-iwW7vos6KwKAdpagKOgciOuA4qSl8Xc5mmiJz2VzsQqUvSO1mua.T47t8fCJQSw3l3y_p4GnPN5dJgtuFxQVVg; cf_clearance=DmIuiKQdAzSxiGmHbeyXNv_gvpn.PeWqHqvmEl96.NE-1712620755-1.0.1.1-bLVQmQ6QgZDjHwUibkR7D.T20OTAVc8z6uib45f6iLP2r6SnIk5x5b8EY.eaKbKsq6ujNsOIVQioOWy.ZIhjdA; _ga_L7MJCSDHKV=GS1.1.1712620755.1.1.1712620768.0.0.0; _ga=GA1.1.426143995.1712620755","Host": "neal.fun","Referer": "https://neal.fun/infinite-craft/","Sec-Fetch-Dest": "empty","Sec-Fetch-Mode": "cors","Sec-Fetch-Site": "same-origin","Sec-GPC": "1","TE": "trailers","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"}

        headers = json.loads(headers_str)
    print(headers)

    # remove everything from &headers= onwards
    base_url = url.split("&headers=")[0]

    http = urllib3.PoolManager()
    response = http.request("GET", base_url, headers=headers)
    
    return {
        "statusCode": response.status,
        "body": response.data
    }

print(lambda_handler({
    "url": "https://neal.fun/api/infinite-craft/pair?first=Water&second=Fire&headers={\"Accept\": \"*/*\",\"Accept-Encoding\": \"gzip, deflate, br\",\"Accept-Language\": \"en-US,en;q=0.5\",\"Connection\": \"keep-alive\",\"Cookie\": \"__cf_bm=VTD.yb16LSAMEU135hG848uASIgj0suVqwH.6F5S2os-1712620754-1.0.1.1-iwW7vos6KwKAdpagKOgciOuA4qSl8Xc5mmiJz2VzsQqUvSO1mua.T47t8fCJQSw3l3y_p4GnPN5dJgtuFxQVVg; cf_clearance=DmIuiKQdAzSxiGmHbeyXNv_gvpn.PeWqHqvmEl96.NE-1712620755-1.0.1.1-bLVQmQ6QgZDjHwUibkR7D.T20OTAVc8z6uib45f6iLP2r6SnIk5x5b8EY.eaKbKsq6ujNsOIVQioOWy.ZIhjdA; _ga_L7MJCSDHKV=GS1.1.1712620755.1.1.1712620768.0.0.0; _ga=GA1.1.426143995.1712620755\",\"Host\": \"neal.fun\",\"Referer\": \"https://neal.fun/infinite-craft/\",\"Sec-Fetch-Dest\": \"empty\",\"Sec-Fetch-Mode\": \"cors\",\"Sec-Fetch-Site\": \"same-origin\",\"Sec-GPC\": \"1\",\"TE\": \"trailers\",\"User-Agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0\"}"
},None))