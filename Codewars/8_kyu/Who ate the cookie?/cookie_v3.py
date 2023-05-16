def cookie(x):
    return "Who ate the last cookie? It was {}!".format({str: 'Zach', bool: 'the dog'}.get(type(x), 'Monica'))
