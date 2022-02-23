def encrypt(text, n): # correct work
    if n <= 0:
        return text
    else:
        s = text[:]
        for k in range(n):
            s = s[-len(text):]
            for i in range(1, len(text), 2):
                s += s[i]
            for i in range(0, len(text), 2):
                s += s[i]

        return s[-len(text):]


def decrypt(text, n): # no correct worc for some events
    if n <= 0:
        return text
    else:
        l_i = "!"
        s = list(text[:-1])
        for k in range(n):
            text = s[-len(text):]
            text1 = text[:len(text) // 2]
            text2 = text[len(text) // 2:]
            for i in range(len(text)):
                if i % 2 == 1:
                    s.append(text2.pop(-1))
                else:
                    if text1:
                        s.append(text1.pop(-1))
                    else:
                        break
        if n % 2 != 0:
            a = s[-len(text):]
            st = "".join(a[::-1])
        else:
            st = "".join(s[-len(text):])
        return st + l_i


print(encrypt("This is a test!", 0))   #"This is a test!")
print(encrypt("This is a test!", 1))    # "hsi  etTi sats!")
print(encrypt("This is a test!", 2))    # "s eT ashi tist!")
print(encrypt("This is a test!", 3))      #" Tah itse sits!")
print(encrypt("This is a test!", 4))     # "This is a test!")
print(encrypt("This is a test!", -1))    # "This is a test!")
print(encrypt("This kata is very interesting!", 1) == "hskt svr neetn!Ti aai eyitrsig")

print(decrypt("This is a test!", 0))    # "This is a test!")
print(decrypt("hsi  etTi sats!", 1))     # "This is a test!")
print(decrypt("s eT ashi tist!", 2))     # "This is a test!")
print(decrypt(" Tah itse sits!", 3))     # "This is a test!")
print(decrypt("This is a test!", 4))     # "This is a test!")
print(decrypt("This is a test!", -1))     # "This is a test!")
print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1))
