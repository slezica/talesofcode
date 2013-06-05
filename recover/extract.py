import codecs, collections, code, slugify, HTMLParser
from lxml import etree, html

HTMLP = HTMLParser.HTMLParser()
Entry = collections.namedtuple('Entry', ['name', 'date', 'body'])

feed = etree.parse('atom.xml')

def preprocess(body):
	x = html.fromstring(body)

	for figure in x.xpath('//figure[@class="code"]'):
		code = figure.xpath('//td[@class="code"]')[0]

		plain = ']    ' + (
			''.join(code.itertext()).replace('\n', '\n    ')
		)[:-4]
		
		x.replace(figure, html.fromstring(plain))

	return html.tostring(x)

def recover():
	for entry_node in feed.findall('entry'):
		get = lambda x: entry_node.find(x).text

		entry = Entry(
			name = slugify.slugify(unicode(get('title'))),
			date = get('updated').split('T')[0],
			body = preprocess(get('content'))
		)

		filename = 'posts/' + entry.date + '-' + entry.name + '.markdown'

		with codecs.open(filename, 'w', 'utf-8') as f:
			f.write(entry.body[5:-7])

recover()

# def list_tags():
# 	tags = set()

# 	def scan(node):
# 		tags.add(node.tag)

# 		for child in node:
# 			scan(child)

# 	for content in feed.findall('entry/content'):
# 		result = scan(html.fromstring(content.text))

# 	print tags
# list_tags()
# code.interact(local = locals())
