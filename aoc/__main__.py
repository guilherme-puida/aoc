import argparse
import contextlib
import importlib
import itertools
import os
import pathlib
import sys
import time
import urllib.request

BASE_DIR = pathlib.Path(__file__).parent.resolve()
CURRENT_YEAR = 2023

@contextlib.contextmanager
def timer():
    start_time = end_time = time.perf_counter()
    yield lambda: end_time - start_time
    end_time = time.perf_counter()

def scaffold_solution(year: int, day: int):
    solution_path = BASE_DIR / "solutions" / f"y{year}d{day:02d}.py"
    if solution_path.exists():
        return

    base_solution = """from aoc.lib.base_solution import BaseSolution


class Solution(BaseSolution):
    def setup(self):
        pass

    def part_one(self):
        pass

    def part_two(self):
        pass"""

    solution_path.parent.mkdir(parents=True, exist_ok=True)
    solution_path.write_text(base_solution)

def get_input_path(year: int, day: int):
    return pathlib.Path(__file__).parent.resolve() / "inputs" / f"y{year}d{day:02d}.txt"

def get_solution_module(year: int, day: int):
    return importlib.import_module(f"aoc.solutions.y{year}d{day:02d}")

def download_input(year: int, day: int):
    aoc_cookie = os.environ.get("AOC_COOKIE")
    if not aoc_cookie:
        raise ValueError("please set AOC_COOKIE")

    url = f"https://adventofcode.com/{year}/day/{day}/input"

    request = urllib.request.Request(url)
    request.add_header("Cookie", f"session={aoc_cookie}")

    response = urllib.request.urlopen(request)
    data = response.read()

    output_path = get_input_path(year, day)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(data.decode("utf-8"))

def prepare_solution(year: int, day: int):
    scaffold_solution(year, day)

def run_solution(year: int, day: int):
    scaffold_solution(year, day)
    input_path = get_input_path(year, day)
    if not input_path.exists():
        download_input(year, day)

    module = get_solution_module(year, day)
    solution = module.Solution(input_path.read_text().strip())

    with timer() as setup_time:
        solution.setup()
    print(f"Setup took {setup_time():.6f} seconds.")

    with timer() as part_one_time:
        part_one_result = solution.part_one()
    print(f"Part one: {part_one_result} in {part_one_time():.6f} seconds.")

    with timer() as part_two_time:
        part_two_result = solution.part_two()
    print(f"Part two: {part_two_result} in {part_two_time():.6f} seconds.")

def check_result(expected, actual):
    if expected is None:
        print("INFO: expected is None")
        return False

    if expected != actual:
        print(f"FAILED: {expected=} {actual=}")
        return False

    return True

def run_all():
    years = range(2015, CURRENT_YEAR + 1)
    days = range(1, 25 + 1)
    failures = 0

    for year, day in itertools.product(years, days):
        try:
            module = get_solution_module(year, day)
        except ModuleNotFoundError:
            continue

        print(f"== {year} {day:02d} ==")
        input_path = get_input_path(year, day)
        if not input_path.exists():
            download_input(year, day)
        solution = module.Solution(input_path.read_text().strip())

        with timer() as setup_time:
            solution.setup()
        print(f"Setup took {setup_time():.6f} seconds.")

        with timer() as part_one_time:
            part_one_result = solution.part_one()
        print(f"Part one: {part_one_result} in {part_one_time():.6f} seconds.")
        if not check_result(solution.result_one, part_one_result):
            failures += 1

        with timer() as part_two_time:
            part_two_result = solution.part_two()
        print(f"Part two: {part_two_result} in {part_two_time():.6f} seconds.")
        if not check_result(solution.result_two, part_two_result):
            failures += 1

    return failures

def main():
    parser = argparse.ArgumentParser(description="Advent of Code helper")

    subparsers = parser.add_subparsers(title="commands", dest="command", help="available commands")

    download_parser = subparsers.add_parser("download", help="download input for given day")
    download_parser.add_argument("year", type=int, help="event's year")
    download_parser.add_argument("day", type=int, help="which day will be downloaded")

    run_parser = subparsers.add_parser("run", help="run solution")
    run_parser.add_argument("year", type=int, help="event's year")
    run_parser.add_argument("day", type=int, help="which day will run")

    run_all_parser = subparsers.add_parser("runall", help="run and test all solutions")

    args = parser.parse_args()

    if args.command == "download":
        download_input(args.year, args.day)
    elif args.command == "run":
        run_solution(args.year, args.day)
    elif args.command == "runall":
        with timer() as all_solutions_time:
            failures = run_all()

        print(f"Ran all solutions in {all_solutions_time():.6f} with {failures} failures")
        sys.exit(failures)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
