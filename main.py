import tkinter as tk
import customtkinter as ctk
import datetime
import locale
from PIL import Image
from funcs import get_weather

root = ctk.CTk()
root.title('Weather App')
root.iconphoto(False, tk.PhotoImage(file="weather_icon.png"))
root.geometry("800x500+700+300")
root.resizable(False, False)
root.configure(fg_color="#fb8c00")

# Top Frame
top_frame = ctk.CTkFrame(root, width=800, height=50, fg_color="#212121", corner_radius=0)
top_frame.pack(fill="x")

# City Label
city_font = ctk.CTkFont(size=15)
city_label = ctk.CTkLabel(top_frame, text="", text_color="#fff", font=city_font)
city_label.place(x=20, y=10)

# Search
search_entry = ctk.CTkEntry(top_frame, placeholder_text="Type city...")
search_entry.place(x=520, y=10)

search_btn = ctk.CTkButton(top_frame, text="Search", width=100, command=lambda: get_weather(elements=window_elements))
search_btn.place(x=670, y=10)
search_entry.bind("<Return>", lambda event: get_weather(elements=window_elements))

# Start Content Frame
start_content_frame = ctk.CTkFrame(root, corner_radius=0, fg_color="#fb8c00")
start_content_frame.pack(fill="both", expand=True)

welcome_font = ctk.CTkFont(size=30)
welcome_label = ctk.CTkLabel(start_content_frame, text="Добро пожаловать в программу показа погоды", text_color="#fff",
                             font=welcome_font)
welcome_label.place(relx=0.5, rely=0.5, anchor="center")

# Content Frame
content_frame = ctk.CTkFrame(root, corner_radius=0, fg_color="#fb8c00")
# content_frame.pack(fill="both", expand=True)

# Date
locale.setlocale(locale.LC_TIME, "ru")
curr_date = datetime.datetime.now().strftime("%a, %B %d")
date_font = ctk.CTkFont(size=20)
date_label = ctk.CTkLabel(content_frame, text=curr_date, text_color="#fff", font=date_font)
date_label.place(relx=0.5, y=30, anchor="center")

# City
city_cnt_label = ctk.CTkLabel(content_frame, text="Название города", text_color="#fff", font=date_font)
city_cnt_label.place(relx=0.5, y=60, anchor="center")

# Icon
weather_icon = ctk.CTkImage(light_image=Image.open("weather_icon.png"), size=(150, 150))
weather_icon_label = ctk.CTkLabel(content_frame, text="", image=weather_icon)
weather_icon_label.place(x=30, y=120)

# Temperature
temp_font = ctk.CTkFont(size=50)
temp_label = ctk.CTkLabel(content_frame, text="25 °C", text_color="#fff", font=temp_font)
temp_label.place(x=200, y=150)

# Other data
data_textbox_font = ctk.CTkFont(size=15, weight="bold")
data_textbox = ctk.CTkTextbox(content_frame, fg_color="#e65100", text_color="#fff", width=300, height=250,
                              font=data_textbox_font, spacing3=5, wrap="word", activate_scrollbars=False)
data_textbox.place(x=450, y=150)

window_elements = {
    "search_entry": search_entry,
    "content_frame": content_frame,
    "start_content_frame": start_content_frame,
    "city_label": city_label,
    "city_cnt_label": city_cnt_label,
    "temp_label": temp_label,
    "data_textbox": data_textbox,
}

root.mainloop()

# pyinstaller --noconfirm --onedir --windowed -i "C:\Users\Admin\Desktop\Python\weather_gui\weather_app.ico" --distpath "C:\Users\Admin\Desktop\Python\weather_gui\program" --add-data "C:\Users\Admin\Desktop\Python\venv\Lib\site-packages\customtkinter;customtkinter\" --add-data "C:\Users\Admin\Desktop\Python\weather_gui\weather_icon.png;." main.py
