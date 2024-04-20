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

if __name__ == "__main__":
    input_str = sys.stdin.readline().strip()
    reversed_str = reverse_string(input_str)
    sys.stdout.write(reversed_str)
