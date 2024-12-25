from flask import Flask, render_template, request
import requests
import datetime

app = Flask(__name__, template_folder='templates-sql')

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
    return report_filename  # Oluşturulan rapor dosyasının adını döndür

@app.route('/')
def index():
    return render_template('index-sql.html')

@app.route('/run_test', methods=['POST'])
def run_test():
    base_url = request.form['base_url']
    path = request.form['path']
    payload_file = "sql.txt"  # SQL Injection payload'larını içeren dosyanın adı

    results = []

    try:
        # SQL Injection payload'larını içeren dosyayı oku
        with open(payload_file, 'r') as file:
            payloads = file.read().splitlines()

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

    report_filename = save_report(results)
    return render_template('result-sql.html', result=results, report_filename=report_filename)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
