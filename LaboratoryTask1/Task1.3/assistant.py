from display import Display

class Assistant:
    def __init__(self, assistantName: str):
        self.assistantName = assistantName
        self.assignedDisplays: List[Display] = []

    def assignDisplay(self, display: Display):
        self.assignedDisplays.append(display)

    def assist(self):
        if not self.assignedDisplays:
            print("No displays assigned.")
            return
        for i in range(len(self.assignedDisplays) - 1):
            comparison = self.assignedDisplays[i].compareWithMonitor(self.assignedDisplays[i + 1])
            print(comparison)
            print() 

    def buyDisplay(self, display: Display):
        if display in self.assignedDisplays:
            self.assignedDisplays.remove(display)
            return display
        else:
            print(f"{display.model} is not assigned to the assistant.")
            return None