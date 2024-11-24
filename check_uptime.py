import requests

# Ganti dengan API Key dan Monitor ID kamu
API_KEY = 'u2305023-73e94b25a40b1adef76f569f'
MONITOR_ID = 'ur2305023-e5f614b05c435ca8095fbb29'

def check_uptime():
    try:
        response = requests.get('https://api.uptimerobot.com/v2/getMonitors', params={
            'api_key': API_KEY,
            'monitors': MONITOR_ID,
            'format': 'json'
        })

        data = response.json()

        if data['stat'] == 'ok':
            monitor = data['monitors'][0]
            status = monitor['status']
            friendly_status = {
                0: "Down",
                1: "Up",
                2: "Paused",
                8: "Unknown"
            }.get(status, "Unknown")

            print(f"Status Monitor: {friendly_status}")
        else:
            print("Error fetching monitor status:", data['error_message'])

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    check_uptime()
