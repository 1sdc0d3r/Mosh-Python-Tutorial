from pathlib import Path
path = Path("emails")
print(path.exists())


# path = Path("emails")
# path.mkdir()
# print(path.exists())
# path.rmdir()

path = Path()
for file in path.glob("*.py"):
    print(file)
