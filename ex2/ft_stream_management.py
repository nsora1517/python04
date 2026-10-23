import sys
import typing


def main() -> None:
    args = sys.argv
    if len(args) != 2:
        print(f"Usage: {args[0]} <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{args[1]}'")
    try:
        file: typing.IO[str] = open(args[1])
    except OSError as e:
        print(f"[STDERR] Error opening file '{args[1]}': {e}", file=sys.stderr)
        return
    try:
        text: str = file.read()
        print("---")
        print()
        print(text)
        print("---")
    except (UnicodeDecodeError, OSError) as e:
        print(f"[STDERR] Error reading file '{args[1]}': {e}", file=sys.stderr)
        return
    finally:
        file.close()
        print(f"File '{args[1]}' closed.")
    print()
    print("Transform data:")
    print("---")
    print()
    new_text = ""
    for line in text.splitlines():
        new_text = new_text + line + "#\n"
    print(new_text)
    print("---")
    print("Enter new file name (or empty): ", end="", flush=True)
    try:
        enter_new_file = sys.stdin.readline().rstrip("\n")
    except (UnicodeDecodeError, OSError) as e:
        print(f"[STDERR] Error reading standard input: {e}", file=sys.stderr)
        return
    if enter_new_file == "":
        print("Not saving data.")
    else:
        print(f"Saving data to '{enter_new_file}'")
        try:
            new_file = open(enter_new_file, "w")
        except OSError as e:
            print(f"[STDERR] Error opening file '{enter_new_file}': {e}",
                  file=sys.stderr)
            print("Data not saved.")
            return
        try:
            new_file.write(new_text)
            new_file.close()
        except OSError as e:
            print(f"[STDERR] Error writing file '{enter_new_file}': {e}",
                  file=sys.stderr)
            print("Data not saved.")
            return
        finally:
            new_file.close()
        print(f"Data saved in file '{enter_new_file}'.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt", file=sys.stderr)
