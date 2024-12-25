from flask import Flask, render_template, request
from recon import create_report
import os

app = Flask(__name__, template_folder='templates-recon')  # Template klasörünün adını belirtin

@app.route('/')
def index():
    return render_template('index-recon.html')  # Template adını direkt olarak belirtin

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        target_url = request.form['target_url']
        report_dir = "raporlar"
        create_report(target_url, report_dir)

        # En son oluşturulan raporu al
        latest_report = get_latest_report(report_dir)
        
        return render_template('result-recon.html', target_url=target_url, latest_report=latest_report)

def get_latest_report(report_dir):
    # Raporların kaydedileceği dizini kontrol et
    if not os.path.exists(report_dir):
        return None

    # Rapor dosyalarını listele ve sırala
    reports = [f for f in os.listdir(report_dir) if f.startswith('kesif_raporu_')]
    reports.sort()

    # En son oluşturulan raporu döndür
    if reports:
        latest_report_path = os.path.join(report_dir, reports[-1])
        with open(latest_report_path, 'r') as f:
            latest_report = f.read()
        return latest_report
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True, port=5003)
