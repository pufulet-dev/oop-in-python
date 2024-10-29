import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Task1.2')))
from file_reader import FileReader
from text_data import TextData


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please enter the names of the text files to be processed.")
        sys.exit(1)

    FileReader = FileReader()

    for file_path in sys.argv[1:]:
        try:
            text_content = FileReader.readFileIntoString(file_path)  
            text_data = TextData(text_content, file_path)
            print(text_data)  
        except Exception as e:
            print(f"Error processing file '{file_path}': {e}")