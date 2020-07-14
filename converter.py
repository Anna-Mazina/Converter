import html
import os
import glob
import pypandoc
import shutil

if not os.path.isdir("Обработано"):
     os.mkdir("Обработано")

new_name = 'a'
for infile in glob.glob("*.html"):
     doc = pypandoc.convert_file(infile, 'md', outputfile= new_name + ".md")
     new_name += '1'

for a in glob.glob('*.md'):
    new_name = '{}_{}'.format(os.path.basename(os.path.dirname(a)), os.path.basename(a))
    shutil.move(a, os.path.join('Обработано', new_name))


print('Готово')