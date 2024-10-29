import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Task1.1')))
from display import Display
from assistant import Assistant

if __name__ == "__main__":
    display1 = Display(width=1920, height=1080, ppi=92, model="Samsung")
    display2 = Display(width=2560, height=1440, ppi=109, model="Nokia")
    display3 = Display(width=3840, height=2160, ppi=163, model="Pixel")
    display4 = Display(width=4000, height=2000, ppi=120, model="DisplayPixel")

    assistant = Assistant("Display Assistant")
    assistant.assignDisplay(display1)
    assistant.assignDisplay(display2)
    assistant.assignDisplay(display3)
    assistant.assignDisplay(display4)

    print("Assisting with display comparisons:")
    assistant.assist()

    print("Buying Display B:")
    bought_display = assistant.buyDisplay(display2)
    if bought_display:
        print(f"Bought: {bought_display.model}")

    print("Assisting after buying a display:")
    assistant.assist()