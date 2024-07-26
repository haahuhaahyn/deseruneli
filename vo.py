from charset_normalizer import detect

text = "Hello, world!"

encoding = detect(text)
print(encoding)
