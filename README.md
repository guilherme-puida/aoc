# AOC

My solutions to Advent Of Code. Written in Python without any external
dependencies.

## Usage

### Download Input

```shell
python -m aoc download <year> <day>
```

This expects an `AOC_COOKIE` enviroment variable containing your
account's cookie.  Inputs are stored in `aoc/inputs/yYYYYdDD.txt`.

### Run Solution

```shell
python -m aoc run <year> <day>
```

Solutions are stored in `aoc/solutions/yYYYYdNN.py`.

### Run and Test

```shell
python -m aoc runall
```

This runs and tests all implemented solutions.