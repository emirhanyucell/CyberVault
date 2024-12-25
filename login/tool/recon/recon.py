# recon.py

import os
import requests
import socket
import dns.resolver
import whois
import ssl
import http.client

def get_ip_address(domain):
    try:
        # Verilen domainin IP adresini alır.
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

def get_dns_records(domain):
    try:
        # Verilen domainin DNS kayıtlarını alır.
        answers = dns.resolver.query(domain, 'A')
        return [rdata.address for rdata in answers]
    except dns.resolver.NXDOMAIN:
        return None

def get_http_headers(url):
    try:
        # Verilen URL'nin HTTP başlıklarını alır.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.head(url, headers=headers)
        headers = response.headers
        return headers
    except requests.exceptions.RequestException:
        return None

def get_ssl_info(domain, port=443):
    try:
        # Verilen domainin SSL/TLS bilgilerini alır.
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                return cert
    except Exception as e:
        return None

def get_whois_info(domain):
    try:
        # Verilen domainin WHOIS bilgilerini alır.
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        return None

def check_robots_txt(url):
    try:
        # Verilen URL'nin robots.txt dosyasının içeriğini kontrol eder.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(url + '/robots.txt', headers=headers)
        if response.status_code == 200:
            content = response.text
            return content
        else:
            return f"robots.txt not found (HTTP Status Code: {response.status_code})"
    except requests.exceptions.RequestException:
        return None

def create_report(target_url, report_dir):
    # Raporu kaydetmek için bir dosya adı oluşturur.
    report_num = 1
    while True:
        report_file = os.path.join(report_dir, f"kesif_raporu_{report_num}.txt")
        if not os.path.exists(report_file):
            break
        report_num += 1

    # Raporu oluşturur ve ilgili bilgileri dosyaya yazar.
    with open(report_file, 'w') as f:
        f.write(f"Keşif Raporu {report_num} - {target_url}\n")
        f.write("\nIP Adresi:\n")
        f.write(f"{get_ip_address(target_url)}\n\n")
        f.write("DNS Kayıtları:\n")
        dns_records = get_dns_records(target_url)
        if dns_records:
            for record in dns_records:
                f.write(f"{record}\n")
        else:
            f.write("DNS kayıtları bulunamadı.\n")
        f.write("\nHTTP Başlıkları:\n")
        headers = get_http_headers(target_url)
        if headers:
            for key, value in headers.items():
                f.write(f"{key}: {value}\n")
        else:
            f.write("HTTP başlıkları bulunamadı.\n")
        f.write("\nSSL/TLS Bilgileri:\n")
        ssl_info = get_ssl_info(target_url)
        if ssl_info:
            f.write(str(ssl_info))
        else:
            f.write("SSL/TLS bilgileri bulunamadı.\n")
        f.write("\nWHOIS Bilgileri:\n")
        whois_info = get_whois_info(target_url)
        if whois_info:
            f.write(str(whois_info))
        else:
            f.write("WHOIS bilgileri bulunamadı.\n")
        f.write("\nrobots.txt İçeriği:\n")
        robots_txt = check_robots_txt(target_url)
        if robots_txt:
            f.write(robots_txt)
        else:
            f.write("robots.txt not found.\n")

    return f"kesif_raporu_{report_num}.txt"

if __name__ == '__main__':
    # Kullanıcıdan hedef URL'yi alır.
    target_url = input("Lütfen hedef URL'yi girin: ")
    report_dir = "raporlar"
    
    # Raporların kaydedileceği dizini oluşturur.
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # Keşif raporu oluşturur ve kaydeder.
    latest_report_name = create_report(target_url, report_dir)
    print(f"Keşif raporu oluşturuldu: {os.path.join(report_dir, latest_report_name)}")
