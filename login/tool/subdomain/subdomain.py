import requests

def search_subdomains(domain_name):
    found_subdomains = []

    try:
        with open("subdomains-list.txt", 'r') as file:
            directories = file.read().splitlines()

        for sub in directories:
            sub_domain = f"http://{sub}.{domain_name}"

            try:
                response = requests.get(sub_domain, timeout=5)
            except requests.ConnectionError:
                pass
            else:
                if response.status_code == 200:
                    found_subdomains.append(sub_domain)

    except FileNotFoundError:
        print("Dizin dosyası bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

    return found_subdomains

def save_report(found_subdomains, domain_name):
    if found_subdomains:
        print("\nBulunan subdomain'ler:")
        for subdomain in found_subdomains:
            print(subdomain)

        with open(f"{domain_name}_subdomains_report.txt", "w") as report_file:
            report_file.write("Bulunan Subdomain'ler:\n")
            for subdomain in found_subdomains:
                report_file.write(subdomain + '\n')
        print(f"Rapor oluşturuldu: {domain_name}_subdomains_report.txt")
    else:
        print("Herhangi bir subdomain bulunamadı.")

def search():
    domain_name = input("Domain adını girin (örneğin, google.com): ")
    found_subdomains = search_subdomains(domain_name)
    save_report(found_subdomains, domain_name)

if __name__ == "__main__":
    search()
