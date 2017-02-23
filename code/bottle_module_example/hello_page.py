from bottle import Bottle

hello_page = Bottle()

@hello_page.get('/hello')
def hello_page_get():
    return 'Hello Page!'


