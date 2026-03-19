from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

carpeta = "C:/ruta/a/la/carpeta"

archivos = {
    "a.txt": "alpha.txt",
    "b.txt": "beta.txt"
}

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        nombre = os.path.basename(event.src_path)
        if nombre in archivos:
            nuevo = archivos[nombre]
            os.rename(event.src_path, os.path.join(carpeta, nuevo))
            print("Renombrado", nombre)

observer = Observer()
observer.schedule(Handler(), carpeta, recursive=False)
observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()

observer.join()