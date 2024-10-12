def connect(wlan, netcreds, hostname="hello", reconnects=3):
    wlan.active(True)
    if not wlan.isconnected():
        print("connecting to network", netcreds[0])
        wlan.config(reconnects=reconnects)
        wlan.config(dhcp_hostname=hostname)
        wlan.connect(*netcreds)
        while not wlan.isconnected():
            pass

    if not wlan.isconnected():
        return None

    return wlan.ipconfig("addr4")[0]
