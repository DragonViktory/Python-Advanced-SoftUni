from abc import ABC, abstractmethod


class Rule(ABC):
    @abstractmethod
    def execute(self, file_obj):
        pass


REQUIRED_HEADERS = set(["name", "age", "address", "job"])


class HeaderRule(Rule):
    def execute(self, file_obj):
        if REQUIRED_HEADERS.issubset(file_obj.headers):
            return True
        return False


class NameRule(Rule):
    def execute(self, file_obj):
        all_names = file_obj['name'].all()
        for name in all_names:
            try:
                first, last = name.split()
                continue
            except:
                return False


class AgeRule(Rule):
    def execute(self, file_obj):
        all_ages = file_obj['age'].all()
        for age in all_ages:
            if age < 10:
                return False


RULES = [HeaderRule, NameRule]


class FileReceiver:
    def __init__(self):
        self.file = None

    def upload(self, file):
        self.file = file

    def process_file(self, rules):
        for rule in rules:
            rule.execute()

    def display_result(self):
        pass


class File:
    pass


fr = FileReceiver()
file = File()
fr.upload(file)
fr.process_file(rules=RULES)
