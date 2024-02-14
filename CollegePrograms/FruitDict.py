FRUIT_DICT={
    'Orange':'Oranage',
    'Gurava':'Green',
    'Banana':'Yellow',
    'Apple':'Red',
    'Mango':'Green',
}
FLOWER_DICT={
    'Sunflower':'Yellow',
    'Lily':'Purple',
    'Rose':'Red',
    'Tulip':'white',
    'Marigold':'Orange',
}

print(FRUIT_DICT)
print(FLOWER_DICT)
L0=[x for x in (FRUIT_DICT.keys()) if FRUIT_DICT[x] is 'Red']+[x for x in (FLOWER_DICT.keys()) if FLOWER_DICT[x] is 'Red']
print(L0)