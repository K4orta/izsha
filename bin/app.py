import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from watchdog.observers import Observer
import izsha

def watch(path):
    event_handler = izsha.OnReplay(izsha.process_replay, print_out)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print("Izsha is watching {0} for new replays...".format(path))
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def print_out(output):
    print(output)

def main():
    print("Izsha starting...")
    path = sys.argv[2] if len(sys.argv) > 1 else '.'
    command = sys.argv[1]
    commands = {
        'watch': watch
    }

    if command in commands:
        commands[command](path)
    else:
        print("invalid command: {0}".format(command))

if __name__ == "__main__":
    main()