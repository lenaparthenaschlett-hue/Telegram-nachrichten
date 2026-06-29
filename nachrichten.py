import requests
import os
from datetime import datetime

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = "8885507228"

def sende_nachricht(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    antwort = requests.post(url, json={"chat_id": CHAT_ID, "text": text})
    print(antwort.json())

jetzt = datetime.now()
stunde = jetzt.hour
minute = jetzt.minute
datum = jetzt.strftime("%d.%m")

# TÄGLICH – 07:30 Uhr
if stunde == 7 and minute >= 30 and minute < 31:
    sende_nachricht(
        "Morgen Lena 🌸\n\n"
        "Kurzer Reminder an dich selbst:\n\n"
        "✨ Du bist eine tolle Freundin.\n"
        "✨ Du bist eine tolle Schwester.\n"
        "✨ Du bist eine sehr tolle Partnerin.\n\n"
        "💛 Du darfst vertrauen – und vertraust auch heute in eine Partnerschaft."
    )

# 10. JULI – 08:00 Uhr
if datum == "10.07" and stunde == 8 and minute < 1:
    sende_nachricht(
        "Guten Morgen Lena 🌅\n\n"
        "Du schaffst es heute zu vertrauen.\n"
        "Fokus auf dich – du bist bei dir.\n\n"
        "Wünsch Moritz von Herzen viel Spaß. 💛\n"
        "Du kannst ihm vertrauen."
    )

# 10. JULI – 21:00 Uhr
if datum == "10.07" and stunde == 21 and minute < 1:
    sende_nachricht(
        "Hallo Lena 💜\n\n"
        "Du vertraust Moritz zu hundert Prozent.\n"
