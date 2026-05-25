MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/',
}

# Reverse lookup: Morse → character
TEXT_CODE = {v: k for k, v in MORSE_CODE.items()}


def text_to_morse(text: str) -> str:
    """Convert plain text to Morse code."""
    result = []
    for char in text.upper():
        if char in MORSE_CODE:
            result.append(MORSE_CODE[char])
        else:
            raise ValueError(f"Character '{char}' has no Morse code equivalent.")
    return ' '.join(result)


def morse_to_text(morse: str) -> str:
    """Convert Morse code back to plain text.

    Words are separated by ' / ' and letters by single spaces.
    Example: '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'
    """
    result = []
    words = morse.strip().split(' / ')
    for word in words:
        letters = word.split()
        for symbol in letters:
            if symbol in TEXT_CODE:
                result.append(TEXT_CODE[symbol])
            else:
                raise ValueError(f"Unknown Morse sequence: '{symbol}'")
        result.append(' ')
    return ''.join(result).strip()


def main():
    print("=" * 50)
    print("       MORSE CODE CONVERTER")
    print("=" * 50)
    print("1. Text  → Morse")
    print("2. Morse → Text")
    print("3. Quit")
    print("-" * 50)

    while True:
        choice = input("\nChoose an option (1/2/3): ").strip()

        if choice == '1':
            text = input("Enter text: ")
            try:
                morse = text_to_morse(text)
                print(f"\nMorse code:\n{morse}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            print("Tip: Separate letters with spaces, words with ' / '")
            morse = input("Enter Morse code: ")
            try:
                text = morse_to_text(morse)
                print(f"\nDecoded text:\n{text}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()