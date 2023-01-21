text = "universidad tecnologica de leon"

print(type(text))
print(text.lower())
print(text.upper())
print(text.title())
print(text.find("de"))
print(text.count("a"))

text2 = text.replace("e" , "3")
print(text2)

text3 = text.split(" ")
print(text3)