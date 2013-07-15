import os, re, time
from watchdog.events import FileSystemEventHandler

class OnReplay(FileSystemEventHandler):
    def __init__(self, process_callback, on_finish):
        self.__process_callback = process_callback
        self.__on_finish = on_finish
        self.__replay_ext_re = re.compile("(.SC2Replay$)", re.I)

    def on_modified(self, event):
        if os.path.isfile(event.src_path) and self.__replay_ext_re.search(event.src_path):
            time.sleep(1)
            self.__on_finish(self.__process_callback(event.src_path))

    def on_created(self, event):
        if os.path.isfile(event.src_path) and self.__replay_ext_re.search(event.src_path):
            time.sleep(1)
            self.__on_finish(self.__process_callback(event.src_path))