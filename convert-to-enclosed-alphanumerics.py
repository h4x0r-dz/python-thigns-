def enclose_alphanumerics(text_to_convert):
    # Mapping of alphanumeric characters to their enclosed equivalents
    enclosed_map = {
        '0': '⓪', '1': '①', '2': '②', '3': '③', '4': '④',
        '5': '⑤', '6': '⑥', '7': '⑦', '8': '⑧', '9': '⑨',
        'a': 'ⓐ', 'b': 'ⓑ', 'c': 'ⓒ', 'd': 'ⓓ', 'e': 'ⓔ',
        'f': 'ⓕ', 'g': 'ⓖ', 'h': 'ⓗ', 'i': 'ⓘ', 'j': 'ⓙ',
        'k': 'ⓚ', 'l': 'ⓛ', 'm': 'ⓜ', 'n': 'ⓝ', 'o': 'ⓞ',
        'p': 'ⓟ', 'q': 'ⓠ', 'r': 'ⓡ', 's': 'ⓢ', 't': 'ⓣ',
        'u': 'ⓤ', 'v': 'ⓥ', 'w': 'ⓦ', 'x': 'ⓧ', 'y': 'ⓨ',
        'z': 'ⓩ'
    }

    # Convert each character using the map, leaving non-alphanumeric characters unchanged
    enclosed_text = ''.join(enclosed_map.get(char.lower(), char) for char in text_to_convert)
    
    return enclosed_text

# Main execution block
if __name__ == "__main__":
    # Prompt user for input
    user_input = input("Enter text to convert to enclosed alphanumerics: ")
    # Convert and display the result
    print(enclose_alphanumerics(user_input))
