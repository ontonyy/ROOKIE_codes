import requests
import folium
from pyfiglet import Figlet


def get_info_by_ip(ip="127.0.0.1"):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()

        data = {
            "[IP]": response.get("query"),
            "[Country]": response.get("country"),
            "[City]": response.get("city"),
            "[Internet provider]": response.get("isp"),
            "[Org]": response.get("org"),
            "[Region name]": response.get("regionName"),
            "[ZIP]": response.get("zip"),
            "[Lat]": response.get("lat"),
            "[Lon]": response.get("lon"),
        }

        for k, v in data.items():
            print(f"{k} : {v}")

        area = folium.Map(location=[response.get("lat"), response.get("lon")])
        area.save(f"{response.get('query')}_{response.get('city')}.html")

    except requests.exceptions.ConnectionError:
        print("[!] Check your connection!")


def main():
    preview_text = Figlet(font="slant")
    print(preview_text.renderText("IP INFO"))
    ip = input("Please enter a target IP: ")
    get_info_by_ip(ip)


if __name__ == '__main__':
    main()
