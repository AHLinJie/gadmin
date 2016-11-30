# coding=utf-8
"""
output the data
"""


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fount = open('output.html', 'w')
        fount.write('<html>')
        fount.write('<body>')
        fount.write('<table>')
        for data in self.datas:
            fount.write('<tr>')
            fount.write('<td>%s</td>' % data['url'].encode('utf-8'))
            fount.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fount.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fount.write('</tr>')
        fount.write('</table>')
        fount.write('</body>')
        fount.write('<html>')
        fount.close()
