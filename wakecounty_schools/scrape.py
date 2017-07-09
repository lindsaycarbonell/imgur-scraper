import requests
import urllib

base_url = 'http://wwwgis2.wcpss.net/addressLookup/index.php?'

req_StreetName = 'Remington+Oaks+Cir+Cary'
req_StreetTemplateValue = 'REM'
req_StreetNumber = '4000'
req_StreetZipCode = '27519'

request = 'SelectAssignment%7C2016%7CCURRENT=2016-17&DefaultAction=SelectAssignment%7C2016%7CCURRENT&DefaultAction=SelectAssignment%7C2017%7CCURRENT&CatchmentCode=CA+0386.2&StreetName=' + req_StreetName + '&StreetTemplateValue=' + req_StreetTemplateValue + '&StreetNumber=' + req_StreetNumber + '&StreetZipCode=' + req_StreetZipCode;

url = base_url + request

response = requests.get(url)
html = response.content

print html
