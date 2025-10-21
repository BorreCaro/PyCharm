while (s := input()) != "*":
    string = "".join(c.lower() for c in s if c.isalpha())
    print("Y" if string == string[::-1] else "N")