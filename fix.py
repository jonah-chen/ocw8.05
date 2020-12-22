"""Fixing my really bad LaTeX codes and formatting when I started this project."""

f = open("main.tex")
main = f.read()
f.close()

dirs = []
while 1:
    start = main.find("\\input{") + len("\\input{")
    if start < len("\\input{"):
        break
    main = main[start:]
    end = main.find("}")
    path = main[:end]
    if path.find(".tex") < 0:
        path += ".tex"
    dirs.append(path)

for path in dirs:
    is_begin = True
    f = open(path)
    latex = f.read()
    f.close()
    print("OLd\n")
    print(latex)
    fixed = ""
    while 1:
        loc = latex.find("$$")
        if loc < 0:
            fixed += latex
            break
    
        if is_begin:
            fixed += latex[:loc] + "\\begin{equation}\n\t"
            is_begin = False
        else:
            fixed += latex[:loc] + "\n\\end{equation}"
            is_begin = True
        latex = latex[loc+2:]
    print("New\n")
    print(fixed)

    i = input("Do you want to overwrite [y/N]")
    if i == "y":
        f = open(path, "w")
        f.write(fixed)
        print("Write succesful")
    
        



print(dirs)