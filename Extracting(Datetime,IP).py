import glob,os
from datetime import datetime, timedelta
import sys
import pickle
import time

start_time = time.time()
Data = []
folder_path = 'F:/sepideh-data/foxtel-12-12'
output_path = 'G:/pickles/foxtel-12-12/Data-foxtel-12-12.pkl'


list_of_file_path =[]
for filename in sorted(os.listdir(folder_path)):
    file_path= folder_path+'/'+filename  #file path to each log file is set.
    list_of_file_path.append(file_path)
for file_path in list_of_file_path:
   with open(file_path) as input:
         lines = input.readlines()
         for line in lines:
             string_after_open_brac = line.split('[')[1]
             date = string_after_open_brac.split(']')[0]
             date = date.split('.')[0]
             format = "%Y-%m-%dT%H:%M:%S"
             datetime_obj = datetime.strptime(date, format)
             IP = line.split('-')[0].replace(' ', '')
             Data.append([datetime_obj,IP])

print("--- %s seconds ---" % (time.time() - start_time))
pickle.dump( Data, open( output_path,'wb') )
