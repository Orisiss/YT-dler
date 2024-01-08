import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
from tkinter import ttk

def download_video():
    video_url = url_entry.get()
    download_path = path_entry.get()
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=download_path)
        status_label.config(text="Téléchargement terminé!")
    except Exception as e:
        status_label.config(text="Erreur lors du téléchargement: " + str(e))

def browse_directory():
    directory = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, directory)

style = ttk.Style()
style.theme_use("clam")

# Création de la fenêtre principale
window = tk.Tk()
window.title("Téléchargeur de vidéos YouTube")
window.geometry("800x250")  # Définir la taille de la fenêtre

# Création des widgets
url_label = ttk.Label(window, text="URL de la vidéo:")
url_label.pack()

url_entry = ttk.Entry(window, width=50)
url_entry.pack()

path_label = ttk.Label(window, text="Chemin de téléchargement:")
path_label.pack()

path_entry = ttk.Entry(window, width=50)
path_entry.pack()

browse_button = ttk.Button(window, text="Parcourir", command=browse_directory)
browse_button.pack()

download_button = ttk.Button(window, text="Télécharger", command=download_video)
download_button.pack()

status_label = ttk.Label(window, text="")
status_label.pack()

# Ajouter des indications pour utiliser l'application
instructions_label = ttk.Label(window, text="Entrez l'URL de la vidéo YouTube et le chemin de téléchargement, puis cliquez sur le bouton Télécharger.")
instructions_label.pack()

# Lancement de la boucle principale
window.mainloop()