from flask import Flask, render_template, request
import socket

app = Flask(__name__, template_folder='templates-nmap')

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

@app.route('/')
def index():
    return render_template('index-nmap.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        target_domain = request.form['target_domain']
        start_port = int(request.form['start_port'])
        end_port = int(request.form['end_port'])

        ip_address = socket.gethostbyname(target_domain)
        open_ports = scan_ports(ip_address, start_port, end_port)

        if open_ports:
            save_report(target_domain, ip_address, open_ports)
            return render_template('result-nmap.html', target_domain=target_domain, open_ports=open_ports)
        else:
            return render_template('result-nmap.html', target_domain=target_domain, message="Açık port bulunamadı.")
    except socket.gaierror:
        return render_template('result-nmap.html', message="Hedef domainin IP adresi alınamadı.")
    except Exception as e:
        return render_template('result-nmap.html', message=f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    app.run(debug=True, port=5004)
