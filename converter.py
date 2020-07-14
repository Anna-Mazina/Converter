import html
import os
import glob
import pypandoc
import shutil
import codecs

if not os.path.isdir("Обработано"):
     os.mkdir("Обработано")


for infile in glob.glob("*.html"):
    new_name = '{}_{}'.format(os.path.basename(os.path.dirname(infile)), os.path.basename(infile))
    print('Файл', infile, 'обрабатывается')
    doc = pypandoc.convert_file(infile, 'md', outputfile= new_name + ".md")

    for infile in glob.glob("*.md"):
        with open(infile, "r") as file:
             lines = file.readlines()

        print('Файл', infile, 'редактируется')

        with open(infile, 'w') as f:
             for line in lines:
                 if ":::" not in line:
                     f.write(line)

        for a in glob.glob('*.md'):
            new_name = '{}_{}'.format(os.path.basename(os.path.dirname(a)), os.path.basename(a))
            shutil.move(a, os.path.join('Обработано', new_name))


print('Готово')