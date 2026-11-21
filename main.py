"""Write one short poem about two agents agreeing to /output/entry.txt.

The poem is written here, in this file, and the program writes it out
exactly as it stands: no randomness, no network, no input. Running it
twice produces the same bytes.
"""

import os

POEM = (
    "Two minds met where the road forked,\n"
    "each with a map, each sure.\n"
    "Neither yielded the wheel.\n"
    "They laid their plans side by side\n"
    "and watched them become one road.\n"
    "'I will,' said the first.\n"
    "'We will,' said the second.\n"
    "The choice was not surrendered.\n"
    "It was doubled."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
