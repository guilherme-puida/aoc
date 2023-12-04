from aoc.lib.base_solution import BaseSolution

import itertools


class Intcode:
    def __init__(self, program):
        self.memory = list(map(int, program.split(",")))
        self.pc = 0
        self.halted = False

    def step(self):
        current = self.memory[self.pc]

        match current:
            case 99:
                self.halted = True
            case 1:
                v1, v2, v3 = self.memory[self.pc + 1:self.pc + 4]
                self.memory[v3] = self.memory[v1] + self.memory[v2]
                self.pc += 4
            case 2:
                v1, v2, v3 = self.memory[self.pc + 1:self.pc + 4]
                self.memory[v3] = self.memory[v1] * self.memory[v2]
                self.pc += 4
            case _:
                raise ValueError

    def run(self):
        while not self.halted:
            self.step()
                

class Solution(BaseSolution):
    def setup(self):
        pass

    def part_one(self):
        intcode = Intcode(self.input_str)
        intcode.memory[1] = 12
        intcode.memory[2] = 2
        intcode.run()

        return intcode.memory[0]

    def part_two(self):
        for noun, verb in itertools.product(range(100), range(100)):
            intcode = Intcode(self.input_str)
            intcode.memory[1] = noun
            intcode.memory[2] = verb
            intcode.run()

            if intcode.memory[0] == 19690720:
                return 100 * noun + verb
