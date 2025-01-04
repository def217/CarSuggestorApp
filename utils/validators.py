def validate_menu_option(prompt, count):
    while True:
        try:
            choice = int(input(f"\n{prompt}"))
            if 0 <= choice <= count:
                return choice
            else:
                print(f"Invalid input. Please enter a number (1 - {count}).")
        except (ValueError, TypeError):
            print(f"Invalid input. Please enter a number (1 - {count}).")