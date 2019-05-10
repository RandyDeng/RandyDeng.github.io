"""
Auto generates gallery.yml file.
Assumes there are 2 folders with same image names: gallery and gallery_fullsize
Generate the reduced size images using resize.py
"""

import os

link_folder = 'assets/images/gallery'
link2_folder = 'assets/images/gallery_fullsize'
yml_file = '_data/gallery.yml'
root = os.path.dirname(os.getcwd())

link_path = os.path.join(root, link_folder)
yml_path = os.path.join(root, yml_file)
file_names = os.listdir(link_path)

contents = open(yml_path, 'w')
for file_name in file_names:
    link = os.path.join(link_folder, file_name)
    link2 = os.path.join(link2_folder, file_name)

    content = ('- name: {}\n'
               '  link: {}\n'
               '  link2: {}\n\n'.format(
                   file_name, link, link2))
    contents.write(content)
contents.close()