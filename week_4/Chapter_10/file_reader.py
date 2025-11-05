from pathlib import Path

path = Path('week_4/Chapter_10/pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)