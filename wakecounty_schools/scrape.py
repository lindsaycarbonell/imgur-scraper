import requests
import urllib
from bs4 import BeautifulSoup
import re

base_url = 'http://wwwgis2.wcpss.net/addressLookup/index.php?'

req_StreetName = 'Remington+Oaks+Cir+Cary'
req_StreetTemplateValue = 'REM'
req_StreetNumber = '4000'
req_StreetZipCode = '27519'

request = 'SelectAssignment%7C2016%7CCURRENT=2016-17&DefaultAction=SelectAssignment%7C2016%7CCURRENT&DefaultAction=SelectAssignment%7C2017%7CCURRENT&CatchmentCode=CA+0386.2&StreetName=' + req_StreetName + '&StreetTemplateValue=' + req_StreetTemplateValue + '&StreetNumber=' + req_StreetNumber + '&StreetZipCode=' + req_StreetZipCode;

url = base_url + request

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")

def find_schools():

    td_tags = soup.find_all('td', attrs={'width': '33%'})

    pattern_es = re.compile(r'ES')
    pattern_ms = re.compile(r'MS')
    pattern_hs = re.compile(r'HS')
    # pattern_cap = re.compile(r'<font color="red">')

    for td in td_tags:
        es_match = re.search(pattern_es, str(td.contents), flags=0)
        ms_match = re.search(pattern_ms, str(td.contents), flags=0)
        hs_match = re.search(pattern_hs, str(td.contents), flags=0)
        # cap_match = re.search(pattern_cap, str(td.contents), flags=0)

        if es_match:
            src_match = re.search(pattern_es, str(td.contents), flags=0)
            es = str(td.contents)[5:src_match.end()]
        elif ms_match:
            src_match = re.search(pattern_ms, str(td.contents), flags=0)
            ms = str(td.contents)[5:src_match.end()]
        elif hs_match:
            src_match = re.search(pattern_hs, str(td.contents), flags=0)
            hs = str(td.contents)[5:src_match.end()]

        # if cap_match:
        #     src_match = re.search(pattern_cap, str(td.contents), flags=0)


    print str(es) + '\n' + str(ms) + '\n' + str(hs)

find_schools()
