import sys

def main():
    # 1     2   3   4
    # --key k --val v
    key = sys.argv[2]
    value = sys.argv[4] if len(sys.argv) > 4 else ""

    storage = {}

    if value:
        storage.update({key: value})
    else:
        pass

    print(storage[key])

main()
