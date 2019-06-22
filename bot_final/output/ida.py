import random
import time

from dan import NoData

####To check file modified time###
import os.path, time
file_path =  'output.txt'
target_time = os.path.getmtime(file_path)

### The register server host, you can use IP or Domain.
host = 'iottalk2.tw'

### [OPTIONAL] The register port, default = 9992
# port = 9992

### [OPTIONAL] If not given or None, server will auto-generate.
# device_name = 'Dummy_Test'

### [OPTIONAL] If not given or None, DAN will register using a random UUID.
### Or you can use following code to use MAC address for device_addr.
# from uuid import getnode
# device_addr = "{:012X}".format(getnode())
#device_addr = "aa8e5b58-8a9b-419b-b8d5-72624d61108d"

### [OPTIONAL] If not given or None, this device will be used by anyone.
username = 'nicozhou'

### The Device Model in IoTtalk, please check IoTtalk document.
device_model = 'Dummy_Device'

### The input/output device features, please check IoTtalk document.
idf_list = ['Dummy_Sensor']
### Set the push interval, default = 1 (sec)
### Or you can set to 0, and control in your feature input function.
push_interval = 10  # global interval
interval = {
    'Dummy_Sensor': 3,  # assign feature interval
}

def register_callback():
    print('register successfully')


def Dummy_Sensor():
    global target_time
    modify_time = os.path.getmtime(file_path)
    if modify_time != target_time:
        target_time = modify_time
        f = open("output.txt", "r")
        str_out = f.read()
        return str_out
    else:
        return NoData
