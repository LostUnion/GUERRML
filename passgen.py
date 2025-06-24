import string
import random
import argparse

class PASSGEN:
    @staticmethod
    def get_password(length: int, use_special_chars: bool) -> str:
        base_chars = string.ascii_letters + string.digits
        if use_special_chars:
            base_chars += string.punctuation
        return ''.join(random.choice(base_chars) for _ in range(length))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PASSWORD GENERATION")
    parser.add_argument("--length", "-len", type=int, default=10, help="Length of the password")
    parser.add_argument("--characters", "-char", help="Include special characters")
    parser.add_argument("--count", "-c", type=int, default=1, help="Count passwords")
    args = parser.parse_args()
    for _ in range(args.count):
        print(PASSGEN.get_password(args.length, args.characters))