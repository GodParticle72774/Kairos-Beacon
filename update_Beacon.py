# update_beacon.py (Version 2 - Now with multi-line support)
# A script to add a new, timestamped entry to the Kairos-Beacon journal.

import datetime


def add_new_entry():
    """Prompts for a multi-line entry and appends it to README.md."""

    today = datetime.date.today()
    formatted_date = today.strftime("%m/%d/%y")

    print("Please type your new journal entry. Type '_end_' on a new line by itself to finish.")

    lines = []
    while True:
        line = input()
        # The loop will stop if the user just types '_end_' and nothing else.
        if line.strip() == '_end_':
            break
        lines.append(line)

    # Join all the collected lines together into a single block of text.
    new_text = "\n".join(lines)

    # Don't save if the user didn't enter any text.
    if not new_text.strip():
        print("\nNo text entered. Aborting.")
        return

    full_entry = f"\n\n---\n\n**{formatted_date}**\n\n{new_text}"

    try:
        with open("README.md", "a", encoding="utf-8") as f:
            f.write(full_entry)

        print("\nSuccess! Your new entry has been added to the beacon's log (README.md).")
        print("Don't forget to commit and push the changes to GitHub to make it live.")

    except FileNotFoundError:
        print("\nError: README.md not found. Make sure this script is in the same folder.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    add_new_entry()