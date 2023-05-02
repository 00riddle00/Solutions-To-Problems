def well(x):
    match x.count('good'):
        case 0: return 'Fail!'
        case 1 | 2: return 'Publish!'
    return 'I smell a series!'
