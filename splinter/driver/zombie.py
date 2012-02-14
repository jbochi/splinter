from pythonzombie import Browser
from pythonzombie.browser import verb

from splinter.element_list import ElementList
from splinter.driver import DriverAPI

class ZombieBrowser(DriverAPI):
    def __init__(self, *args, **kwargs):
        self.zombie = Browser()

    @property
    def title(self):
        return self.zombie.text("title")

    @property
    def url(self):
        return self.zombie.location

    @property
    def html(self):
        return self.zombie.html

    @verb
    def visit(self, url):
        self.zombie.visit(url)

    @verb
    def back(self):
        self.zombie.client.wait('back')

    @verb
    def forward(self):
        self.zombie.client.json('browser.history.forward()')

    def reload(self):
        return self.zombie.client.wait('reload')

    @verb
    def type(self, field, value, slowly=False):
        self.zombie.fill(field, value)

    def find_by_css(self, css):
        return ElementList(self.zombie.css(css))

    def find_by_id(self, id):
        return self.find_by_css('#' + id)

    def find_by_name(self, name):
        return self.find_by_id(name)

    def find_link_by_text(self, text):
        return self.find_by_css('*:contains(%s)' % (text,))

    def find_link_by_partial_text(self, text):
        return self.find_by_css('*:contains(%s)' % (text,))

    def find_link_by_href(self, href):
        return self.find_by_css('a[href="%s"]' % href)

    def find_link_by_partial_href(self, href):
        return self.find_by_css('a[href*="%s"]' % href)

    def find_by_xpath(self, xpath):
        result = self.zombie.client.json('browser.xpath("%s")' % (xpath,))
        elements = result['value']
        return ElementList(elements)

