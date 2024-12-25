import requests
from datetime import datetime

def discover_directories(base_url, wordlist, results):
    try:
        # Dizin listesini oku
        with open(wordlist, 'r') as file:
            directories = file.read().splitlines()

        # Her bir dizin kelimesi üzerinde döngü yap
        for directory in directories:
            # URL'yi oluştur
            url = f"{base_url}/{directory}"

            # HTTP GET isteği gönder
            response = requests.get(url)

            # Eğer sayfa bulunursa (HTTP status code 200), sonuçları ekrana ve listeye ekle
            if response.status_code == 200:
                result = f"[{response.status_code}] Found: {url}"
                print(result)
                results.append(result)

    except FileNotFoundError:
        print("Dizin dosyası bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def save_report(results):
    # Zaman damgası alınarak rapor dosyasının adı oluşturuluyor
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    report_filename = f"directory_discovery_report_{timestamp}.txt"

    # Sonuçları rapor dosyasına yaz
    with open(report_filename, 'w') as report_file:
        report_file.write("Directory Discovery Report\n")
        report_file.write("=" * 40 + "\n\n")

        for result in results:
            report_file.write(result + "\n")

    print(f"Rapor oluşturuldu: {report_filename}")

def main():
    # Kullanıcıdan giriş al
    base_url = input("Dizin keşfi yapılacak domaini girin (örneğin, http://xxx.com): ")
    wordlist = input("Dizinlerin taranacağı kelime listesi dosyasını girin (örneğin, dizin.txt): ")
    results = []

    try:
        # Dizin keşfi fonksiyonunu çağır
        discover_directories(base_url, wordlist, results)
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

    # Eğer herhangi bir sonuç bulunamazsa kullanıcıya bilgi ver
    if not results:
        print("Herhangi bir sonuç bulunamadı.")

    # Sonuçları rapor dosyasına kaydet
    save_report(results)

if __name__ == "__main__":
    main()
