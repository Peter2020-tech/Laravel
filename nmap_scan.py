import nmap

def scan_target_ports(target_ip):
    nm = nmap.PortScanner()
    nm.scan(target_ip, arguments='-p 1-65535')
    open_ports = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            for port in nm[host][proto]:
                open_ports.append(port)
    return open_ports

target_ip = "104.17.235.27-32"
open_ports = scan_target_ports(target_ip)
print("Open ports on target for attack:", open_ports)
