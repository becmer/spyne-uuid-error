from lxml import etree

def test(path):
    f = open(path, 'r')
    t = etree.parse(f)
    f.close()
    s = etree.XMLSchema(t)

if __name__ == '__main__':
    test('tns.xsd')