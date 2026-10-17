import sys
import typing


def main() -> None:
    args = sys.argv
    if len(args) != 2:
        print(f"Usage: {args[0]} <file>")
        return

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{args[1]}'")
    try:
        file: typing.IO[str] = open(args[1])
    except OSError as e:
        print(f"Error opening file '{args[1]}': {e}")
        return
    try:
        text: str = file.read()
        print("---")
        print()
        print(text)
        print("---")
    except (UnicodeDecodeError, OSError) as e:
        print(f"Error reading file '{args[1]}': {e}")
    finally:
        file.close()
        print(f"File '{args[1]}' closed.")


if __name__ == "__main__":
    main()
