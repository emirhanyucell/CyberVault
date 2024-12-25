import requests
import datetime

def test_sql_injection(base_url, path, payload):
    try:
        # SQL Injection kontrolü
        url = f"{base_url}/{path}?id={payload}"
        response = requests.get(url)

        if "error" in response.text.lower():
            result = f"Potansiyel SQL Injection Zafiyeti Tespit Edildi! (Payload: {payload}) - URL: {url}"
            print(result)
            return result

    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def save_report(results):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    report_filename = f"sql_injection_report_{timestamp}.txt"

    with open(report_filename, 'w') as report_file:
        report_file.write("SQL Injection Test Raporu\n")
        report_file.write("=" * 40 + "\n\n")

        for result in results:
            report_file.write(result + "\n")

    print(f"Rapor oluşturuldu: {report_filename}")

def main():
    base_url = input("Test yapılacak domaini girin (örneğin, http://xxx.com): ")
    paths = input("Test yapılacak URL kısımlarını aralarında virgül bırakarak girin (örneğin, id,user): ").split(',')
    payload_file = "sql.txt"  # SQL Injection payload'larını içeren dosyanın adı

    results = []

    try:
        # SQL Injection payload'larını içeren dosyayı oku
        with open(payload_file, 'r') as file:
            payloads = file.read().splitlines()

        for path in paths:
            zafiyet_tespiti = False
            # Her bir payload için test et
            for payload in payloads:
                if not zafiyet_tespiti:
                    result = test_sql_injection(base_url, path, payload)
                    results.append(result)

                    # Zafiyet tespiti yapıldıysa, diğer payload'ları aynı URL kısmına sorma
                    if "Potansiyel SQL Injection Zafiyeti Tespit Edildi!" in result:
                        zafiyet_tespiti = True

    except FileNotFoundError:
        print("Payload dosyası bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

    if not results:
        print("Herhangi bir sonuç bulunamadı.")

    save_report(results)

if __name__ == "__main__":
    main()
