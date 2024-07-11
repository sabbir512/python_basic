import sys

if len(sys.argv) != 2:
    print("You are missing command-line argument")
    sys.exit(1)

print(f"hello, {sys.argv[1]}")
sys.exit(0)
