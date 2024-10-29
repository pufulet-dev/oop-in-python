import sys
from file_reader import FileReader
from text_data import TextData

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please enter the name of text file to be processed.")
        sys.exit(1)

    file_path = sys.argv[1]
    file_reader = FileReader()
    text_content = file_reader.readFileIntoString(file_path)

    text_data = TextData(text_content, file_path)
    print(text_data)