# Game Of Life

The `GameOfLife.py` file consists of input of the generation by reading the file `input.txt`, finding the next generation, checking the living neighbors around a cell and outputting the next generation in a file named `output.txt`.

## Usage

### Using in command line

```python
python GameOfLife.py

cat output.txt
```

### Using in Docker container

```docker
docker build --rm -t gameoflife .

docker run --rm -it gameoflife
```

### Running the tests

```python
python GameOfLifeTests.py
```