from bottle import Bottle

help_pages = Bottle()

@help_pages.get('/stuff')
def stuff_get():
    return 'Help about stuff!'

@help_pages.get('/things')
def things_get():
    return 'Help about things!'

if __name__ == '__main__':
    help_pages.run(debug=True)


