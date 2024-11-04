from display import Display

def main():
    display1 = Display(1220, 1080, 220.5, "Samsung")
    display2 = Display(2560, 1040, 309.9, "Nokia")
    display3 = Display(3800, 2060, 151.0, "Pixel")

    output = []
    output.append(display1.compareWithMonitor(display2))
    output.append(display2.compareWithMonitor(display3))
    output.append(display1.compareWithMonitor(display3))

    output_file_path = 'LaboratoryTask1\Task1.1\display_comparisons.txt'
    with open(output_file_path, 'w') as file:
        file.write("\n\n".join(output))

if __name__ == "__main__":
    main()