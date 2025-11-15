def locate_card(cards,query):
    pass

cards = [13,11,10,7,4,3,1,0]
query = 7
output = 3 
result = locate_card(cards,query)


tests = []



test = {
    'input': {
        'cards':[13,11,10,7,4,3,1,0],
        'query':7
    },
    'output':3
}

tests.append(test)

test = {
    'input': {
        'cards':[13,11,10,7,4,3,1,0],
        'query':13
    },
    'output':0
}

tests.append(test)

test = {
    'input': {
        'cards':[13,11,10,7,4,3,1,0],
        'query':0
    },
    'output':7
}

tests.append(test)

test = {
    'input': {
        'cards':[13,11,10,7,4,3,1,0],
        'query':12
    },
    'output':-1
}

tests.append(test)

test = {
    'input': {
        'cards':[-213,-311,-610,-88,-90,-56,-89,-78],
        'query':-610
    },
    'output':2
}

tests.append(test)

test = {
    'input': {
        'cards':[8,8,6,6,7,7,9,6,8,4,5,5],
        'query':8
    },
    'output':0
}

tests.append(test)

test = {
    'input': {
        'cards':[],
        'query':7
    },
    'output':-1
}

tests.append(test)