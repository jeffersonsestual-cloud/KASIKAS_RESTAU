def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("  Invalid choice! Please enter 'y' or 'n'.")


def choose_option(choices):
    while True:
        print("  Choose one:")
        for i, choice in enumerate(choices, 1):
            print(f"    {i}. {choice}")
        raw = input("  Option : ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(choices):
            return choices[int(raw) - 1]
        print("  Invalid option.")