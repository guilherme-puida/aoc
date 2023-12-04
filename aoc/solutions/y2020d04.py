from aoc.lib.base_solution import BaseSolution

import re


class Solution(BaseSolution):
    result_one = 210
    result_two = 131

    def setup(self):
        self.passports = []

        for entry in self.input_str.split("\n\n"):
            passport = {}
            fields = entry.split()

            for field in fields:
                k, v = field.split(":")
                passport[k] = v

            self.passports.append(passport)

    def part_one(self):
        total = 0

        for passport in self.passports:
            if all(x in passport for x in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")):
                total += 1

        return total

    def part_two(self):
        total = 0

        for passport in self.passports:
            if self.is_valid(passport):
                total += 1

        return total
                

    def is_valid(self, passport):
        try:
            byr = int(passport["byr"])
            if byr > 2002 or byr < 1920:
                return False

            iyr = int(passport["iyr"])
            if iyr < 2010 or iyr > 2020:
                return False

            eyr = int(passport["eyr"])
            if eyr < 2020 or eyr > 2030:
                return False

            hgt = passport["hgt"]
            if "cm" in hgt:
                x = int(hgt.removesuffix("cm"))
                if x < 150 or x > 193:
                    return False
            elif "in" in hgt:
                x = int(hgt.removesuffix("in"))
                if x < 59 or x > 76:
                    return False
            else:
                return False

            hcl = passport["hcl"]
            if not re.fullmatch(r"#[0-9a-f]{6}", hcl):
                return False

            ecl = passport["ecl"]
            if ecl not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                return False

            pid = passport["pid"]
            if not re.fullmatch(r"\d{9}", pid):
                return False

            return True
        except (KeyError, ValueError):
            return False
                
