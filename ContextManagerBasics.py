class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


# loading a file
with FileManager('testt.txt', 'w') as f:
    f.write('Test')

print(f.closed)

------------------------------------------------------------------

class File:
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        print(f"Opening {self.name}...")

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.name}...")


with File("Main.py") as file:
    print(file.name)

print("Done")
