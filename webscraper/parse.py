'''
parse.py
Converts JSON data collected form collect_data_1.py and collect_data_2.py into useable features.
Futher parse.py removes outliers and assigns labels to samples.
Features used:
origin
destination 
num_hrs_until_flight
duration_of_flight_in_mins
num_of_stops
overnight_flight
day_of_week_collected
gross_fare
airline
flight_no
'''
import os
import json
import pandas as pd
from pathlib import Path
import parse_utils
from numpy import array

#CONSTANTS BEGINS#
path_seperator = "\\"
folder_path = r"D:\Education stuff\Northwestern University\Fall 2018\Machine Learning\Project\master"
windows = False
if windows != True:
     folder_path = "/Users/Admin/Documents/code/ml/git_2/ml_final_project"
     path_seperator = "/"
processed_file_directory = folder_path + path_seperator + "sample_json" + path_seperator + "processedFiles" + path_seperator
pd.options.mode.chained_assignment = None
#CONSTANTS ENDS#

# VARYING PARAMETERS BEGINS#

departure_dates = ["dept20181130"] #,"dept20181210","dept20181226",]
collected_date_range = "Nov15To30"
# VARYING PARAMETERS ENDS#


class features:
    def __init__(self):
        self.origin = ""
        self.destination = ""
        self.num_hrs_until_flight = 0
        self.duration_of_flight_in_mins = 0
        self.num_of_stops = 0
        self.overnight_flight = ""
        self.day_of_week_collected = 0
        self.gross_fare = 0
        self.airline = ""
        self.flight_no = ""

        self.date_taken = ""
        self.time_taken = ""
        self.dept_date = ""
        self.dept_time = ""
        self.arrival_date = ""
        self.arrival_time = ""
        self.class_value = ""


    def get_csv_header_string(self):
        str_1 = "origin," + \
        "destination," + \
        "num_hrs_until_flight," + \
        "duration_of_flight_in_mins," + \
        "num_of_stops," + \
        "overnight_flight," + \
        "day_of_week_collected," + \
        "gross_fare," + \
        "airline," +  \
        "flight_no," + \
        "date_taken," + \
        "time_taken," + \
        "dept_date," +  \
        "dept_time," + \
        "arrival_date," + \
        "arrival_time," + \
        "Class"

        str = "origin," + \
        "destination," + \
        "num_hrs_until_flight," + \
        "duration_of_flight_in_mins," + \
        "num_of_stops," + \
        "overnight_flight," + \
        "day_of_week_collected," + \
        "gross_fare," + \
        "airline," +  \
        "flight_no," + \
        "Class"
        return str

    def get_csv_entry(self):
        str_ret_1 = \
        self.origin + ',' + \
        self.destination + ',' + \
        str(self.num_hrs_until_flight) + ',' + \
        str(self.duration_of_flight_in_mins) + ',' + \
        str(self.num_of_stops) + ',' + \
        self.overnight_flight + ',' + \
        str(self.day_of_week_collected) + ',' + \
        str(self.gross_fare) + ',' + \
        self.airline + ',' + \
        self.flight_no + ',' + \
        self.date_taken + ',' + \
        self.time_taken + ',' + \
        self.dept_date + ',' + \
        self.dept_time + ',' + \
        self.arrival_date + ',' + \
        self.arrival_time + ',' + \
        self.class_value

        str_ret = \
        self.origin + ',' + \
        self.destination + ',' + \
        str(self.num_hrs_until_flight) + ',' + \
        str(self.duration_of_flight_in_mins) + ',' + \
        str(self.num_of_stops) + ',' + \
        self.overnight_flight + ',' + \
        str(self.day_of_week_collected) + ',' + \
        str(self.gross_fare) + ',' + \
        self.airline + ',' + \
        self.flight_no + ',' + \
        self.class_value

        return str_ret

    def process_data(self):
        for dept_date in departure_dates:
             for x in range(15,31):
                  common_prefix = folder_path + path_seperator + "sample_json" + path_seperator + collected_date_range + path_seperator + \
                  "2018-11-"+str(x)+path_seperator
                  root_dir = common_prefix + dept_date
                  self.dept_date = dept_date
                  for filename in os.listdir(root_dir):
                        self.origin = filename[0:3]
                        self.destination = filename[4:7]
                        handle = None
                        processed_file_name = processed_file_directory + path_seperator + self.origin + "_" + self.destination + ".csv"
                        my_file = Path(processed_file_name)
                        if my_file.is_file(): #file exists
                            handle = open(processed_file_name, 'a+')
                        else:
                            handle = open(processed_file_name, 'w')
                            handle.write(self.get_csv_header_string())
                            handle.write("\n")

                        self.date_taken = "2018-11-"+str(x)
                        self.time_taken = filename[7:15]
                        file = open(root_dir + '/' + filename,'r')
                        json_data = file.read()
                        removed_1 = json_data.replace('\n', '')
                        file.close()

                        try:
                            d = json.loads(removed_1)
                            flight_details_list = d["data"]["onwardflights"]
                        except:
                            print("Error JSON load file {} {}".format(root_dir, filename))
                            handle.close()
                            continue

                        for flight_details in flight_details_list:
                            self.dept_time = flight_details['deptime']
                            self.arrival_date = flight_details['arrdate']
                            self.arrival_time = flight_details['arrtime']

                            self.num_hrs_until_flight = parse_utils.cal_num_hrs_until_flight(self.date_taken, self.time_taken, dept_date, self.dept_time)
                            if self.num_hrs_until_flight  < 0:
                                continue
                            self.duration_of_flight_in_mins = parse_utils.cal_duration_of_filght_in_mins(flight_details['duration'])

                            self.num_of_stops = flight_details['stops']
                            self.overnight_flight = parse_utils.is_overnight_flight(dept_date,self.dept_time,self.arrival_date, self.arrival_time)
                            self.day_of_week_collected = parse_utils.get_day_of_week_collected(self.date_taken,self.time_taken)

                            self.gross_fare = str(flight_details["fare"]["grossamount"])
                            self.airline = flight_details["airline"]
                            self.flight_no = str(flight_details["flightno"])

                            handle.write(self.get_csv_entry())
                            handle.write("\n")

                        handle.close()

    def remove_outliers(self):
        destn = ["ORD_BWI", "ORD_DXB", "ORD_HYD", "ORD_JFK", "ORD_LAX", "ORD_MAA", "ORD_SFO"]

        for file in destn:
            outliers_removed_file = processed_file_directory + path_seperator + file + "_outliers.csv"
            processed_file = processed_file_directory + path_seperator + file + ".csv"
            df = pd.read_csv(processed_file)
            mean = df['gross_fare'].mean()
            new_df = df.loc[df['gross_fare'] <= mean]
            if not os.path.isfile(outliers_removed_file):
                new_df.to_csv(outliers_removed_file, header=self.get_csv_header_string())
            else:
                new_df.to_csv(outliers_removed_file, mode='a', header=False)
            #os.remove(processed_file)



    def combine_files(self):
        destn = ["ORD_BWI","ORD_DXB","ORD_HYD","ORD_JFK","ORD_LAX","ORD_MAA","ORD_SFO"]
        training_data_file = processed_file_directory + path_seperator + "training_data.csv"
        for file in destn:
            classified_file = processed_file_directory + path_seperator + file + "_classified.csv"
            df = pd.read_csv(classified_file)
            if not os.path.isfile(training_data_file):
                df.to_csv(training_data_file, header=self.get_csv_header_string())
            else:
                df.to_csv(training_data_file, mode='a', header=False)
            #os.remove(classified_file)


    def classify(self):
        destn = ["ORD_BWI", "ORD_DXB", "ORD_HYD", "ORD_JFK", "ORD_LAX", "ORD_MAA", "ORD_SFO"]
        for file in destn:
            outliers_removed_file = processed_file_directory + path_seperator + file + "_outliers.csv"
            classified_file = processed_file_directory + path_seperator + file + "_classified.csv"
            df = pd.read_csv(outliers_removed_file)
            df = df.sort_values('num_hrs_until_flight', ascending=True)

            dfList = df['gross_fare'].tolist()
            class_list = []
            min = dfList[0]
            class_list.append("Buy")
            for item in dfList[1:]:
                if item > min:
                    class_list.append("Wait")
                else:
                    class_list.append("Buy")
                    min = item
            class_list_array = array(class_list)
            df["Class"] = class_list_array
            df.to_csv(classified_file, header=self.get_csv_header_string())
            #os.remove(outliers_removed_file)




f = features()
f.process_data()
f.remove_outliers()
f.classify()
f.combine_files()
