import sys
import os

# create tex file first


with open("tmp.tex", "w", encoding="utf8") as out:
    out.write("\\documentclass{article}\n")
    out.write("\\usepackage{float}\n")
    out.write("\\usepackage{graphicx}\n")
    out.write("\\usepackage[a4paper, total={6in, 8in}]{geometry}\n")
    out.write("\\begin{document}\n")
    for image in sys.argv[1:]:
        print(image)
        out.write("\\begin{figure}\n")
        out.write("\\includegraphics[width=\\linewidth, angle=0]{" + image + "}\n")
        out.write("\\end{figure}\n")
        out.write("\\pagebreak\n")
    out.write("\\end{document}\n")
os.system("pdflatex tmp.tex")
