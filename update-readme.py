"""
Adds preview icons to README.md
"""


import glob
import os


def main():
    readme = open('README.md').read()

    while not readme.endswith('\n\n'):
        readme += '\n'

    head, _ = readme.split('## All icons', 1)

    tail = '\n\n'
    for filepath in glob.glob('assets/*_preview.png'):
        _, filename = os.path.split(filepath)

        tail += '##### %s\n' % filename
        tail += '![%s](assets/%s)\n\n' % (filename, filename)

    f = open('README.md', 'w')
    f.write('## All icons'.join([head, tail]))
    f.close()


if __name__ == '__main__':
    main()
