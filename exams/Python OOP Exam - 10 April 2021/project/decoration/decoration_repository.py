class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        for current_decoration in self.decorations:
            if current_decoration == decoration:
                self.decorations.remove(current_decoration)
                return True
        return False

    def find_by_type(self, decoration_type: str):
        for decoration in self.decorations:
            if type(decoration).__name__ == decoration_type:
                return decoration
        return "None"
