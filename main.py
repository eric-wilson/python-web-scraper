import requests

debugging=False

def searchHtmlPages(url: str, qsKeyValues=None, findValues=None):
    foundValues=False
    parameters = ""
    if qsKeyValues:
        for keyValue in qsKeyValues:
            if len(parameters) > 0:
                parameters = f"{parameters}&"
            parameters = f"{parameters}{keyValue['key']}={keyValue['value']}"
        
            
    url = f"{url}?{parameters}"
    if debugging:
        print(url)
        
    stream = requests.get(url)
    html = stream.text

    if findValues:
        for find in findValues:
            if find in html:
                print(f"found: {find} in {url}")
                foundValues=True

    return findValues
    

if __name__ == '__main__':

    qs = [{
                "key":"abc",
                "value":"1234"   
            },
            {
                "key":"def",
                "value":"5678"
            }
            
    ]

    find = ['Feeling Lucky']
            

    searchHtmlPages("https://www.google.com", qs, find)