def encode_runs(text):
    if not text:
        return ""
    encoded = []
    current = text[0]
    count = 1
    for char in text[1:]:
        if char == current:
            count += 1
        else:
            encoded.append(current + str(count))
            current = char
            count = 1
    encoded.append(current + str(count))
    return "".join(encoded)

def main():
    text = input("Enter text: ")
    encoded = encode_runs(text)
    print("Original:", repr(text))
    print("Encoded:", repr(encoded))
    print("Original length:", len(text))
    print("Encoded length:", len(encoded))
    if len(encoded) < len(text):
        print("Encoding is shorter.")
    elif len(encoded) == len(text):
        print("Encoding has the same length.")
    else:
        print("Encoding is not beneficial for this input.")

if __name__ == "__main__":
    main()
