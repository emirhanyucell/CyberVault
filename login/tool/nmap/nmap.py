import socket

def scan_ports(target_host, start_port, end_port):
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    return open_ports

def save_report(target_domain, ip_address, open_ports):
    report_filename = f"{target_domain}_port_scan_report.txt"
    with open(report_filename, 'w') as report_file:
        report_file.write(f"Domain: {target_domain}\n")
        report_file.write(f"IP Adresi: {ip_address}\n")
        report_file.write("\nAçık Portlar:\n")
        for port in open_ports:
            report_file.write(f"{port}\n")
    print(f"Rapor oluşturuldu: {report_filename}")

if __name__ == "__main__":
    target_domain = input("Hedef domain adını girin: ")
    start_port = int(input("Başlangıç portunu girin: "))
    end_port = int(input("Bitiş portunu girin: "))

    try:
        ip_address = socket.gethostbyname(target_domain)
        open_ports = scan_ports(ip_address, start_port, end_port)

        if open_ports:
            print("Açık portlar:")
            for port in open_ports:
                print(port)
            save_report(target_domain, ip_address, open_ports)
        else:
            print("Açık port bulunamadı.")
    except socket.gaierror:
        print("Hedef domainin IP adresi alınamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
