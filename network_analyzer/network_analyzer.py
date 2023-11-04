import psutil
from ip2geotools.databases.noncomercial import DbIpCity
def network_mon():
    conns = psutil.net_connections(kind='inet')
    for conn in conns:
        print(f"==============================================================")
        print(f"Connections found")
        get_process_details(conn.pid)
        print(f"Scanning details in remote ({conn.raddr.ip})")
        show_ip_details(conn.raddr.ip)

def show_ip_details(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")

def get_process_details(pid):
    try:
        process = psutil.Process(pid)

        print(f"[+] Process Name: {process.name()}")
        print(f"[+] Process ID: {pid}")
        print(f"[+] Process Status: {process.status()}")
    except psutil.NoSuchProcess:
        print(f"No process found with PID {pid}")
    except psutil.AccessDenied:
        print(f"Access Denied to process {pid}")

if __name__ == "__main__":
    network_mon()