import glob, re

def replace(matchobj):
    id = matchobj.group(1)
    return '<a class="anchor" id="%s"></a>%s' % (id.lower(), id)

for filename in glob.glob("docs/*.md"):
    data = ''.join((x for x in open(filename)))
    data = re.sub('@([a-zA-Z_]+)', replace, data)
    out = open(filename, 'w')
    out.write(data)
    out.close()
