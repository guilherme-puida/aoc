import argparse
import contextlib
import importlib
import os
import pathlib
import time
import urllib.request

BASE_DIR = pathlib.Path(__file__).parent.resolve()

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

def run_solution(year: int, day: int):
    scaffold_solution(year, day)
    input_path = get_input_path(year, day)
    if not input_path.exists():
        download_input(year, day)

    module = importlib.import_module(f"aoc.solutions.y{year}d{day:02d}")
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

def main():
    parser = argparse.ArgumentParser(description="Advent of Code helper")

    subparsers = parser.add_subparsers(title="commands", dest="command", help="available commands")

    download_parser = subparsers.add_parser("download", help="download input for given day")
    download_parser.add_argument("year", type=int, help="event's year")
    download_parser.add_argument("day", type=int, help="which day will be downloaded")

    run_parser = subparsers.add_parser("run", help="run solution")
    run_parser.add_argument("year", type=int, help="event's year")
    run_parser.add_argument("day", type=int, help="which day will run")

    args = parser.parse_args()

    if args.command == "download":
        download_input(args.year, args.day)
    elif args.command == "run":
        run_solution(args.year, args.day)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
