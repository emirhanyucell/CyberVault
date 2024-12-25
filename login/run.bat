@echo off

cd D:\xamp\htdocs\login\tool\xss\
start "" python app-xss.py

cd D:\xamp\htdocs\login\tool\sql-inj\
start "" python app-sql.py

cd D:\xamp\htdocs\login\tool\recon\
start "" python app-recon.py

cd D:\xamp\htdocs\login\tool\nmap\
start "" python app-nmap.py

cd D:\xamp\htdocs\login\tool\dirsearch\
start "" python app-dirsearch.py

cd D:\xamp\htdocs\login\tool\subdomain\
start "" python app-subdomain.py

echo Bütün komutlar başarıyla çalıştırıldı.
pause
