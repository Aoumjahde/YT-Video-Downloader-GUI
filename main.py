import tkinter
import customtkinter 
from pytube import YouTube


def start_dowload():

        ytlink = link.get()
        try: 
            yt_object = YouTube(ytlink)
            video = yt_object.streams.get_highest_resolution()
            video.download()
            print("Video is downloaded successfully!") 
        except ValueError: 
            print("This Link is Invalid ")


# customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("dark-blue")

windows = customtkinter.CTk()
windows.geometry("720x480")
windows.title("Youtube Video Dowloander")

title = customtkinter.CTkLabel(windows, text="Instert a Youtube Link (Video URL): ",font=("Anton",20,"bold"))
title.pack(padx=10, pady= 10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(windows,width=460, height=40, corner_radius=5,
                                  border_color="Black",textvariable=url_var)
link.pack()

dow_button = customtkinter.CTkButton(windows, text="Download",corner_radius=10,width=90,
                                    height=45,font=("Anton",20,"bold"),fg_color="orange",text_color="Black",
                                    hover_color="brown",command=start_dowload)
dow_button.pack(padx=10, pady =10)
windows.mainloop()  


