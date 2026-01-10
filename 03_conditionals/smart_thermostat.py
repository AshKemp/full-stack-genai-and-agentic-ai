device_status = "offline"
temperature = 35

if device_status == "active":
    if temperature > 35:
        print("warning: high temperature")
    else:
        print("temperature is normal")
else:
    print("Device is offline")