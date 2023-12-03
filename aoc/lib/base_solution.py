class BaseSolution:
    input_str: str
    lines: list[str]

    def __init__(self, input_str: str):
        self.input_str = input_str
        self.lines = input_str.splitlines()

    def setup(self):
        pass

    def part_one(self):
        return None

    def part_two(self):
        return None
