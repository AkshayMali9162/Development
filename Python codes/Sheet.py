
import json
from multiprocessing.sharedctypes import Value
from turtle import pd
import requests
import time
import urllib3
import csv

from lib2to3.pgen2.pgen import DFAState

import pandas as pd
if __name__ == "__main__":

    bearertoken=vra_token('api.mgmt.cloud.vmware.com',"SfXUIlggsLkB0UpDDii6bX0R_hoLaVpjAlQ8jwWdvTwxeWknFwBqHWrgXVz95KZu")

    df = pd.read_excel (r'D:\Users\MALIA04\Desktop\cloudaccremove.xlsx', header=None)

    df_list = df.values.tolist()

    sr = 0

    csvfile = "ganpaticloudacctask2.csv"

    f = open(csvfile,'a')

    writer = csv.writer(f)

    csvfile = csv.writer(f,delimiter=',',quotechar='"')

    for i in range (len(df_list)):

        sr = sr+1

        df = df_list[i]

        new = df[0]

        time.sleep(3)
        bearertoken=vra_token()

    