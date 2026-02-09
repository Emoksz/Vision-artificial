def greet(name, title=""):
    if title:
        return f"Hello, {title} {name}!"
    return f"Hello, {name}!"

name = "Emix"
title = "Papu."

if name.strip():
    print(greet(name, title))
else:
    print("Error: invalid input")
