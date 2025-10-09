# uniq.py
A `uniq`-like program that works **without sorting the input**.

## Usage
```bash
cat FILENAME | python3 uniq.py
```

# Description
The standard uniq command typically requires sorting the input first, for example:
```bash
sort FILENAME | uniq
```
In contrast, this program preserves the original order and can be used as:
```bash
cat FILENAME | python3 uniq.py
```

# Note
Currently, the program reads data only from the standard input.
