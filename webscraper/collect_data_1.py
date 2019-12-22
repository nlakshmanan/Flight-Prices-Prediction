'''
collect_data_1.py 
Script to flight prices for  destinations with IATA code 'SFO', 'JFK', 'LAX' and 'BWI' from 'ORD' for departure dates 
30 Nov 2018 , 10th Dec 2018 and 26 Dec 2018
'''

import price
import datetime
import os
import schedule
import time

path = os.getcwd()

def get_price_formatted(destn_place, deptDate,file_name):
    format = 'json'
    source_place = "ORD"
    seatingclass = 'E'
    arrivalDate = ''
    price.get_price(format, source_place, destn_place, deptDate, seatingclass, arrivalDate,file_name)

def function_collect_data_sfo(destn_place,deptDate):
    source_place = "ORD"
    date_today = datetime.datetime.today().strftime('%Y-%m-%d')
    directory_name = path + '/'+date_today
    if not os.path.isdir(directory_name):
        os.mkdir(directory_name)
    curr_time = str(datetime.datetime.time(datetime.datetime.now()))
    dir_deptDate = directory_name + '/'  + 'dept' + deptDate
    if not os.path.isdir(dir_deptDate):
        os.mkdir(dir_deptDate)
    file_name = dir_deptDate + '/' + source_place + '_' + destn_place + curr_time + '.txt'
    get_price_formatted(destn_place, deptDate, file_name)

def parse_json(file_name,destn_place,deptDate,date_today):
    csv_dir = path + '/' + "csvfiles"
    if not os.path.isdir(csv_dir):
        os.mkdir(csv_dir)




_10th_dec_2018 = '20181210'
_26th_dec_2018 = '20181226'
_30th_nov_2018 = '20181130'

destn_SFO = 'SFO'
destn_new_york = 'JFK'
destn_los_angeles = 'LAX'
destn_washington_dc = 'BWI'
#destn_dubai = 'DXB'
#destn_hyd = "HYD"
#destn_chennai = "MAA"

dept_list = [destn_SFO,destn_new_york,destn_los_angeles,destn_washington_dc]#,destn_dubai,destn_hyd,destn_chennai]


#startTime = datetime.datetime.now()
def job():
    for item in dept_list:
        function_collect_data_sfo(item,_10th_dec_2018)
        function_collect_data_sfo(item,_26th_dec_2018)
        function_collect_data_sfo(item,_30th_nov_2018)
        #time.sleep(15)

#print datetime.datetime.now() - startTime

#schedule.every(240).minutes.do(job)
#schedule.every(4).hours.do(job)
#schedule.every().day.at("10:30").do(job)

#while 1:
#    schedule.run_pending()
#    time.sleep(1)

job()

#I run is almost 10MB of data
#Per day we store 40MB of data
