import psutil
from ip2geotools.databases.noncomercial import DbIpCity
def network_mon():
    conns = psutil.net_connections(kind='inet')
    for conn in conns:
        print(f"==============================================================")
        print(f"Connections found")
        print(f"Scanning details in remote ({conn.raddr.ip})")

def show_ip_details(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")
