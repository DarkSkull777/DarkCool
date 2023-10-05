# Import library yang diperlukan
import argparse
import requests
from colorama import Fore

# Fungsi untuk melakukan scanning pada URL dengan wordlist
def scan_url_with_wordlist(url, wordlist_file):
    try:
        with open(wordlist_file, 'r') as wordlist:
            for line in wordlist:
                path = line.strip()
                full_url = url + path
                response = requests.get(full_url, timeout=5)
                if response.status_code == 200:
                    print(Fore.GREEN + '[Status 200 OK] >>> ' + full_u>
                else:
                    print(Fore.RED + '[Status ' + str(response.status_>
    except requests.exceptions.RequestException as e:
        print(Fore.RED + 'Terjadi kesalahan saat mengakses URL: ' + st>
    except FileNotFoundError:
        print(Fore.RED + 'File wordlist tidak ditemukan: ' + wordlist_>

# Fungsi utama
def main():
    print(Fore.YELLOW + '--------------------------------------------')
    print(Fore.YELLOW + ' Program Scanning URL Website dengan Wordlist>
    print(Fore.YELLOW + '--------------------------------------------')
    url = input(Fore.CYAN + 'Masukkan URL website: ')
    wordlist_file = 'duniaku.txt'  # Nama file wordlist
    scan_url_with_wordlist(url, wordlist_file)

if __name__ == '__main__':
    main()￼Enter
