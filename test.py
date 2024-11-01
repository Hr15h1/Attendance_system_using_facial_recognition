import device
index = 0
device_list = device.getDeviceList()
for device_name in device_list:
    print(f"{index}: {device_name[0]} is connected")
    index += 1