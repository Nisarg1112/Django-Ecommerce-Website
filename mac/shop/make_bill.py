import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "shop/bill.html"
template = templateEnv.get_template(TEMPLATE_FILE)

outputText = template.render(df=d['df'],
                             interest_rate=d['interest_rate'])
html_file = open(str(int(d['interest_rate'] * 100)) + '.html', 'w')
html_file.write(outputText)
html_file.close()
