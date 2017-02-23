from bottle import Bottle

from hello_page import hello_page
from help_pages import help_pages

root_app = Bottle()

@root_app.route('/')
def rootIndex():
    return 'This Is The Home Page'

if __name__ == '__main__':
    root_app.merge(hello_page)
    root_app.mount('/help/',help_pages)
    root_app.run(debug=True)


