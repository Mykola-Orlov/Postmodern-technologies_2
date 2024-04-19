import sys
# функція приймає рядок і виводить його оберненим
def reverse_string(actual_argument):
    try:
        reversed_str = actual_argument[::-1]
        sys.stdout.write(reversed_str)
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)
