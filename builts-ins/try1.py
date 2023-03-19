a = [True, True, 10>11, 27//5 == 6]
print(all(a))
print(any(a))

st = "mani..<sauc ralpH==- @!£$£\f"
print(ascii(st))

print(bin(255))
print(type(bin(64)))
# or!!! (without the prefix)
print(format(14, "b"))

a = ""
print(bool(a))

# breakpoint()
print("nice")

x = "ralph2004"
y = [1,2,5,87,255,254]
print(bytearray(x, "utf16"))
print(bytearray(y))

print(bytes(y))


def hi():
    return "hi"
def ok():
    return "ok"
funcs = [ok, hi, "nice"]
call = [x() for x in funcs if callable(x)]
print(call)

print(chr(21)) # None
print(chr(50))
print(chr(97)) 