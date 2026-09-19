
def run_length_encoding(text, omit = False):
    text = list(text)
    current = text[0]
    count = 0
    encoded = ""
    for c in text:
        if c == current:
            count += 1
        else:
            encoded += current
            if count == 1:
                if not omit:
                    encoded += "1"
            else:
                encoded += str(count)
            current = c
            count = 1
    if count > 1:
        encoded += text[-1] + str(count)
    elif omit:
        encoded += text[-1]
    else:
        encoded += text[-1] + str(count)
    return encoded
