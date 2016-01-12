# reverse_text.py

def reverse_text(text):
    chars = list(text)
    l = len(chars)
    out = [] 
    for i in range(l):
        out.append(chars[l-i-1])
    return ''.join(out)


if __name__ == '__main__':
    in1 = "hello world"
    out1 = reverse_text(in1)
    assert out1 == 'dlrow olleh', "error"

    assert in1[::-1] == 'dlrow olleh', "error"    