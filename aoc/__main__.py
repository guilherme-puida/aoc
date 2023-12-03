import argparse
import importlib
import os
import pathlib
import urllib.request


def get_input_path(day: int):
    return pathlib.Path(__file__).parent.resolve() / "inputs" / f"{day:02d}.txt"

def download_input(day: int):
    aoc_cookie = os.environ.get("AOC_COOKIE")
    if not aoc_cookie:
        raise ValueError("please set AOC_COOKIE")

    url = f"https://adventofcode.com/2023/day/{day}/input"

    request = urllib.request.Request(url)
    request.add_header("Cookie", f"session={aoc_cookie}")

    response = urllib.request.urlopen(request)
    data = response.read()

    output_path = get_input_path(day)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(data.decode("utf-8"))

def run_solution(day: int):
    input_path = get_input_path(day)
    if not input_path.exists():
        download_input(day)

    module = importlib.import_module(f"aoc.solutions.d{day:02d}")
    solution = module.Solution(input_path.read_text().strip())

    print(solution.part_one())
    print(solution.part_two())

def main():
    parser = argparse.ArgumentParser(description="Advent of Code helper")

    subparsers = parser.add_subparsers(title="commands", dest="command", help="available commands")

    download_parser = subparsers.add_parser("download", help="download input for given day")
    download_parser.add_argument("day", type=int, help="which day will be downloaded")

    run_parser = subparsers.add_parser("run", help="run solution")
    run_parser.add_argument("day", type=int, help="which day will run")

    args = parser.parse_args()

    if args.command == "download":
        download_input(args.day)
    elif args.command == "run":
        run_solution(args.day)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
