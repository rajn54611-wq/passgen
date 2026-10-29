#!/usr/bin/env python3
"""Password Generator + Strength Checker"""
import math
import re
import secrets
import string


def generate(length=16, upper=True, digits=True, symbols=True):
    pools = [string.ascii_lowercase]
    if upper:
        pools.append(string.ascii_uppercase)
    if digits:
        pools.append(string.digits)
    if symbols:
        pools.append("!@#$%^&*()-_=+[]{};:,.?")
    # Guarantee at least one character from each chosen pool
    chars = [secrets.choice(p) for p in pools]
    allowed = "".join(pools)
    chars += [secrets.choice(allowed) for _ in range(length - len(chars))]
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def check_strength(pw):
    pool = 0
    if re.search(r"[a-z]", pw):
        pool += 26
    if re.search(r"[A-Z]", pw):
        pool += 26
    if re.search(r"\d", pw):
        pool += 10
    if re.search(r"[^a-zA-Z0-9]", pw):
        pool += 32
    entropy = len(pw) * math.log2(pool) if pool else 0

    tips = []
    if len(pw) < 12:
        tips.append("Use at least 12 characters")
    if not re.search(r"[A-Z]", pw):
        tips.append("Add uppercase letters")
    if not re.search(r"\d", pw):
        tips.append("Add numbers")
    if not re.search(r"[^a-zA-Z0-9]", pw):
        tips.append("Add symbols")
    if re.search(r"(.)\1{2,}", pw):
        tips.append("Avoid repeated characters")
    if pw.lower() in {"password", "123456", "qwerty", "admin", "letmein"}:
        entropy = 0
        tips.append("This is a very common password")

    if entropy < 40:
        label = "Weak"
    elif entropy < 60:
        label = "Medium"
    elif entropy < 80:
        label = "Strong"
    else:
        label = "Very Strong"
    return label, round(entropy, 1), tips


def main():
    while True:
        print("\n=== Password Tool ===")
        print("1. Generate password")
        print("2. Check password strength")
        print("3. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            try:
                n = int(input("Length (default 16): ") or 16)
            except ValueError:
                n = 16
            n = max(8, min(n, 128))
            pw = generate(n)
            label, bits, _ = check_strength(pw)
            print(f"\nPassword: {pw}")
            print(f"Strength: {label} ({bits} bits)")
        elif choice == "2":
            pw = input("Enter password: ")
            label, bits, tips = check_strength(pw)
            print(f"\nStrength: {label} ({bits} bits)")
            for t in tips:
                print(f" - {t}")
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
