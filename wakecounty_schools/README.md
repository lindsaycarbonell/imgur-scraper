# Wake County School Assignment Scraper
Making a scraper to look up addresses to get school assignments for a graphic I'd like to build about distances between addresses and schools that are capped (there are 15 of them in WCPSS right now) and the school a student would have to attend if they couldn't fit into the closest one to their house.

## Progress
- Determined the POST for the site. Example using an address in Cary for Panther Creek High:

`http://wwwgis2.wcpss.net/addressLookup/index.php`

`SelectAssignment%7C2016%7CCURRENT=2016-17&DefaultAction=SelectAssignment%7C2016%7CCURRENT&DefaultAction=SelectAssignment%7C2017%7CCURRENT&CatchmentCode=CA+0386.2&StreetName=Remington+Oaks+Cir+Cary&StreetTemplateValue=REM&StreetNumber=4000&StreetZipCode=27519`

`SelectAssignment|2016|CURRENT:2016-17
DefaultAction:SelectAssignment|2016|CURRENT
DefaultAction:SelectAssignment|2017|CURRENT
CatchmentCode:CA 0386.2
StreetName:Remington Oaks Cir Cary
StreetTemplateValue:REM
StreetNumber:4000
StreetZipCode:27519`

## To do
- Scrape what I want from the page:
  - If the school has an enrollment cap. I can get the actual enrollment cap from [public data](http://data-wake.opendata.arcgis.com/datasets/wake-county-public-schools).
- Build a system for inputting different addresses
  - system must get the first 3 chars of the addresses
  - system must validate the address
    - could use a Google Maps geocoding wrapper like [this one](https://github.com/googlemaps/google-maps-services-python)

## What I've learned so far

## Links used
