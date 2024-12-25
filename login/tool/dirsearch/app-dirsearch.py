from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__, template_folder='templates-dirsearch')

def discover_directories(base_url, wordlist):
    results = []

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

    return results

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
    return report_filename

@app.route('/')
def index():
    return render_template('index-dirsearch.html')

@app.route('/run_test', methods=['POST'])
def run_test():
    base_url = request.form['base_url']
    wordlist = request.form['wordlist']

    # Dizin keşfi fonksiyonunu çağır
    results = discover_directories(base_url, wordlist)

    # Eğer herhangi bir sonuç bulunamazsa kullanıcıya bilgi ver
    if not results:
        results.append("Herhangi bir sonuç bulunamadı.")

    # Sonuçları rapor dosyasına kaydet
    report_filename = save_report(results)

    return render_template('result-dirsearch.html', results=results, report_filename=report_filename)

if __name__ == "__main__":
    app.run(port=5006, debug=True)
