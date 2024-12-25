import requests
from datetime import datetime

def test_xss(base_url, payload):
    try:
        # XSS kontrolü
        url = f"{base_url}?param={payload}"
        response = requests.get(url)

        if payload.lower() in response.text.lower():
            result = f"Potansiyel XSS Tespit Edildi! - URL: {url} - Payload: {payload}"
            print(result)
            return result

    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def save_report(results):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    report_filename = f"xss_test_report_{timestamp}.txt"

    with open(report_filename, 'w', encoding='utf-8') as report_file:
        report_file.write("XSS Test Report\n")
        report_file.write("=" * 40 + "\n\n")

        for result in results:
            report_file.write(result + "\n")

    print(f"Rapor oluşturuldu: {report_filename}")

def main():
    base_url = input("XSS testi yapılacak domaini girin (örneğin, http://xxx.com): ")
    payload_file = "xss.txt"  # XSS payload'larını içeren dosyanın adı
    results = []

    try:
        # XSS payload'larını içeren dosyayı oku
        with open(payload_file, 'r', encoding='utf-8') as file:
            payloads = file.read().splitlines()

        # Her bir payload için test et
        for payload in payloads:
            result = test_xss(base_url, payload)
            if result:
                results.append(result)

    except FileNotFoundError:
        print("Payload dosyası bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

    if not results:
        print("Herhangi bir sonuç bulunamadı.")

    save_report(results)

if __name__ == "__main__":
    main()
