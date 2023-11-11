import datetime
import config
import requests
from tkinter import messagebox
def get_date_time(ts, timezone, dt_format="%H:%M:%S"):
    tz = datetime.timezone(datetime.timedelta(seconds=timezone))
    return datetime.datetime.fromtimestamp(ts, tz=tz).strftime(dt_format)


def get_weather(event="", elements={}):
    params = {
        "appid": config.API_KEY,
        "units": config.UNITS,
        "lang": config.LANG,
        "q": elements["search_entry"].get()
    }
    try:
        r = requests.get(config.API_URL, params=params)
        weather = r.json()
        print_weather(weather, elements)
    except:
        print_weather({"cod": 0, "message": "Не удалось получить данные"}, elements)


def print_weather(data, elements):
    elements["search_entry"].delete(0, "end")
    if data["cod"] != 200:
        messagebox.showerror("Ошибка", data["message"].ljust(50))
        elements["content_frame"].pack_forget()
        elements["start_content_frame"].pack(fill="both", expand=True)
        elements["city_label"].configure(text="")
    else:
        elements["start_content_frame"].pack_forget()
        elements["content_frame"].pack(fill="both", expand=True)
        city = f"{data['name']}, {data['sys']['country']}"
        elements["city_label"].configure(text=city)
        elements["city_cnt_label"].configure(text=city)
        elements["temp_label"].configure(text=f"{data['main']['temp']} °C")
        sunrise_time = get_date_time(data["sys"]["sunrise"], data["timezone"])
        sunset_time = get_date_time(data["sys"]["sunset"], data["timezone"])
        data_text = f"""Местоположение: {city}
Температура: {data['main']['temp']} °C
Атм. давление: {data['main']['pressure']} гПа
Влажность: {data['main']['humidity']}%
Скорость ветра: {data['wind']['speed']} м/с
Погодные условия: {data['weather'][0]['description']}
Восход: {sunrise_time}
Закат: {sunset_time}"""
        elements["data_textbox"].configure(state="normal")
        elements["data_textbox"].delete("0.0", "end")
        elements["data_textbox"].insert('1.0', data_text)
        elements["data_textbox"].configure(state="disabled")

