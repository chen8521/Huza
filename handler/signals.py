from slots.demo import *


def init_signal(app):
    app.bind_signal('a1', a)
    app.bind_signal('a2', b)
    app.bind_signal('a3', c)
    app.bind_signal('a4', d)
