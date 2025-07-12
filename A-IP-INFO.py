import requests
import time
import sys
import os
import webbrowser

# ========== Developer Info ==========
DEVELOPER = "Developed by 4D1B"
YOUTUBE = "https://youtube.com/@kaziadibmahmud?si=TOl_5VDbA-i6oxxT"
GITHUB = "https://github.com/Kazi-Adib-Mahmud/"
FB_LINK = "https://www.facebook.com/share/1Dyx4sxNeg/"
PASSWORD = "4d1baccess"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def open_facebook():
    print("🌐 Opening Facebook link from 4D1B...")
    time.sleep(1)
    webbrowser.open(FB_LINK)

def print_header():
    print("=" * 60)
    print("... A - IP Info ...".center(60))
    print("=" * 60)
    print("🔧 " + DEVELOPER.center(56))
    print("📺 YouTube  : " + YOUTUBE.center(42))
    print("💻 GitHub   : " + GITHUB.center(42))
    print("📘 Facebook : " + FB_LINK.center(42))
    print("=" * 60)

def fake_hacking_animation():
    lines = [
        "🔍 Scanning system integrity...",
        "🔐 Initiating encrypted shell...",
        "🧠 AI Security Bypass initialized...",
        "📡 Connecting to secured node...",
        "💾 Accessing security vault...",
        "🧬 Injecting authentication code...",
        "✅ Access panel unlocked..."
    ]
    for line in lines:
        print(line)
        time.sleep(0.4)

def check_password():
    while True:
        fake_hacking_animation()
        attempt = input("\n🔑 Enter access password: ")
        if attempt == PASSWORD:
            print("\n🟢 ACCESS GRANTED 🟢\n")
            time.sleep(1)
            break
        else:
            print("\n🚫 ACCESS DENIED")
            print("🔁 Try again...\n")
            time.sleep(1)

def get_ip_location(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    try:
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'success':
            print("\n📡 IP Geolocation Info")
            print("-" * 40)
            print(f"🧭 Latitude     : {data['lat']}")
            print(f"🧭 Longitude    : {data['lon']}")
            print(f"🌐 IP Address   : {ip_address}")
            print(f"🌍 Country      : {data['country']}")
            print(f"🏙️ Region       : {data['regionName']}")
            print(f"🏡 City         : {data['city']}")
            print(f"📮 ZIP Code     : {data['zip']}")
            print(f"🌐 ISP          : {data['isp']}")
            print(f"🏢 Organization : {data['org']}")
            print(f"🕓 Timezone     : {data['timezone']}")
        else:
            print(f"❌ Error: {data['message']}")

    except requests.exceptions.RequestException as e:
        print(f"🚫 Request failed: {e}")

# ======= Main Program =======
if __name__ == "__main__":
    clear_screen()
    open_facebook()
    print_header()
    check_password()

    while True:
        ip = input("🔎 Enter an IP address (or type 'exit'): ")
        if ip.lower() == "exit":
            print("\n👋 Thanks for using A - IP Info!")
            break
        get_ip_location(ip)
        print("\n")
        time.sleep(1)