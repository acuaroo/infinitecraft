import requests
import sys

url = "http://localhost:3000/api/headerTransfer"
element1, element2 = sys.argv[1], sys.argv[2]

cookie = "cf_clearance=k9qHZWn3BGPlf.pQPYEekZU8IkPOoiaX5cCXFZW5yOo-1712757082-1.0.1.1-5gfA_LWidskkDzw44d0ozFX.6i.gBuEjTyO4AsPrr47vSZcjiIjz0S2xgk3XC82jGbUs_bmlUl0udl8QRcXU.Q; __cf_bm=X4P0dyZ_0c8.GCYcLasg4NJ7G0acGM_m.ctMDnSOrRI-1712757082-1.0.1.1-GSA32XOGeImDEsAtyDGnmF19QMJEBMNKR.9LK_bj6OAjdLo8fVNOjzBVbxrRRuZacamlJQvD3qZz46lkc0Knyw"
append = f"https://neal.fun/api/infinite-craft/pair?first={element1}&second={element2}&headers=" + "{\"Accept\": \"*/*\",\"Accept-Encoding\": \"gzip, deflate, br\",\"Accept-Language\": \"en-US,en;q=0.5\",\"Connection\": \"keep-alive\",\"Cookie\": \"" + cookie + "\",\"Host\": \"neal.fun\",\"Referer\": \"https://neal.fun/infinite-craft/\",\"Sec-Fetch-Dest\": \"empty\",\"Sec-Fetch-Mode\": \"cors\",\"Sec-Fetch-Site\": \"same-origin\",\"Sec-GPC\": \"1\",\"TE\": \"trailers\",\"User-Agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0\"}"

response = requests.get(url + "?murl=" + append)

if response.status_code == 200:
  print("Request sent successfully")
  print(response.text)
else:
  print("Failed to send request")
  print("Status Code:", response.status_code)
  print("Response:", response.text)
