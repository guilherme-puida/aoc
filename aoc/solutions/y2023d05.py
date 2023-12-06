from aoc.lib.base_solution import BaseSolution
from aoc.lib.range import Range

class Solution(BaseSolution):
    result_one = 340994e26
    result_two = 52210644

    def setup(self):
        seeds, *rest = self.input_str.split("\n\n")
        self.seeds = [int(x) for x in seeds.split(": ")[1].split()]

        self.maps = []

        for m in rest:
            mapping = {}

            for line in m.splitlines()[1:]:
                dest, src, length = (int(x) for x in line.split())
                mapping[src, length] = dest

            self.maps.append(mapping)

    def part_one(self):
        result = []

        for seed in self.seeds:
            result.append(self.solve_one(seed)) 

        return min(result)

    def part_two(self):
        _, *maps = self.input_str.split("\n\n")
        maps = [[list(map(int, line.split())) for line in m.splitlines()[1:]] for m in maps]

        locations = []
        for i in range(0, len(self.seeds), 2):
            ranges = [(self.seeds[i], self.seeds[i] + self.seeds[i + 1])]
            results = []

            for _map in maps:
                while ranges:
                    start_range, end_range = ranges.pop()
                    for target, start_map, _range in _map:
                        end_map = start_map + _range
                        offset = target - start_map

                        if end_map <= start_range or end_range <= start_map:
                            continue
                        if start_range < start_map:
                            ranges.append((start_range, start_map))
                            start_range = start_map
                        if end_map < end_range:
                            ranges.append((end_map, end_range))
                            end_range = end_map
                        results.append((start_range + offset, end_range + offset))
                        break
                    else:
                        results.append((start_range, end_range))
                ranges = results
                results = []

            locations += ranges

        return min(x for x, _ in locations)
        
    def solve_one(self, seed):
        for m in self.maps:
            seed = self.get_next(seed, m)

        return seed 

    def get_next(self, location, mapping):
        for (src, length), dest in mapping.items():
            if src <= location <= src + length - 1:
                return dest + (location - src)

        return location
