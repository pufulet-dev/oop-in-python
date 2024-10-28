class Display:
    def __init__(self, width: int, height: int, ppi: float, model: str):
        self.width = width
        self.height = height
        self.ppi = ppi
        self.model = model

    def compareSize(self, other):
        area_self = self.width * self.height
        area_other = other.width * other.height
        if area_self > area_other:
            return f"{self.model} has a larger display area than {other.model}."
        elif area_self < area_other:
            return f"{other.model} has a larger display area than {self.model}."
        else:
            return f"{self.model} and {other.model} have the same display area."

    def compareSharpness(self, other):
        if self.ppi > other.ppi:
            return f"{self.model} has a sharper display than {other.model}."
        elif self.ppi < other.ppi:
            return f"{other.model} has a sharper display than {self.model}."
        else:
            return f"{self.model} and {other.model} have the same sharpness."

    def compareWithMonitor(self, other):
        comparisons = [f"Comparing {self.model} with {other.model}:"]
        comparisons.append(self.compareSize(other))
        comparisons.append(self.compareSharpness(other))
        return "\n".join(comparisons)