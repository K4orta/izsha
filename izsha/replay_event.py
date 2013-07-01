import os
from watchdog.events import FileSystemEventHandler

class OnReplay(FileSystemEventHandler):
    def __init__(self, process_callback, on_finish):
        self.__process_callback = process_callback
        self.__on_finish = on_finish

    def on_modified(self, event):
        self.__on_finish(self.__process_callback(event.src_path))

    def on_created(self, event):
        self.__on_finish(self.__process_callback(event.src_path))