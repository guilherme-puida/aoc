from aoc.lib.base_solution import BaseSolution


class Solution(BaseSolution):
    result_one = 1749
    result_two = 515

    def setup(self):
        pass

    def part_one(self):
        pc = 0
        acc = 0
        visited = set()

        while pc not in visited:
            visited.add(pc)
            line = self.lines[pc]

            match line.split():
                case ["nop", _]:
                    pc += 1
                case ["acc", x]:
                    acc += int(x)
                    pc += 1
                case ["jmp", x]:
                    pc += int(x)

        return acc

    def part_two(self):
        pc = 0
        acc = 0
        tried_rewriting = set()
        rewrote = False
        visited = set()

        while pc < len(self.lines):
            visited.add(pc)
            line = self.lines[pc]

            match line.split():
                case ["nop", x]:
                    if not pc in tried_rewriting and not rewrote:
                        tried_rewriting.add(pc)
                        rewrote = True
                        pc += int(x)
                    else:
                        pc += 1
                case ["acc", x]:
                    acc += int(x)
                    pc += 1
                case ["jmp", x]:
                    if not pc in tried_rewriting and not rewrote:
                        tried_rewriting.add(pc)
                        rewrote = True
                        pc += 1
                    else:
                        pc += int(x)

            if pc in visited:
                pc = 0
                acc = 0
                visited = set()
                rewrote = False

        return acc
