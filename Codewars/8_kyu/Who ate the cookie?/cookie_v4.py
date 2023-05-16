def cookie(x):
    return "Who ate the last cookie? It was " + {str: 'Zach', bool: 'the dog'}.get(type(x),'Monica') + "!"
