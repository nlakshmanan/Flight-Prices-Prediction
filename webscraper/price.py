'''
price.py
Implements Goibibo API which is called by collect_data_1.py and collect_data_2.py to extract realtime flight price data.
#https://goibibo.3scale.net/admin/access_details
#API documentation https://goibibo.3scale.net/docs
'''
import urllib2
import os


url_browse = ""

APP_ID = "api id goes here"
APP_KEY = "app key goes here"





def get_price(format,source_place,destn_place, deptDate, seatingclass, arrivalDate,file_name):
    #IATA code for airports in USA https://en.wikipedia.org/wiki/List_of_the_busiest_airports_in_the_United_States
    url = 'http://developer.goibibo.com/api/search/'
    data = {'api_id':APP_ID,
            'app_key':APP_KEY,
            'format':format,
            'source':source_place,
            'destination':destn_place,
            'dateofdeparture':deptDate,
            'dateofarrival':arrivalDate,
            'seatingclass':'E',
            'adults':'1',
            'children':'0',
            'infants':'0',
            'counter':'0'
            }
    try:

        #url = "http://developer.goibibo.com/api/search/?app_id=9b7513ef&app_key=1ce2d80882279d272ce8a2319656de45&format=xml&source=ORD&destination=SFO&dateofdeparture=20181115&seatingclass=E&adults=1&children=0&infants=0&counter=0"
        url = "http://developer.goibibo.com/api/search/?app_id=" + APP_ID + "&app_key=" + APP_KEY + "&format=" \
        + data['format'] + "&source=" + data['source'] + "&destination=" + data['destination'] + "&dateofdeparture=" \
        + data['dateofdeparture'] + "&seatingclass=" + data['seatingclass'] + "&adults=" + data['adults'] + "&children=" \
        + data['children'] + "&infants=" + data['infants'] + "&counter=" + data['counter']
        url_browse = urllib2.urlopen(url).read()
    except urllib2.HTTPError:
        print 'There was an ERROR'


    fil = open(file_name, "w")
    fil.write(url_browse)
    fil.close()
