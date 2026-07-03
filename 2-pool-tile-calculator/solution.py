def count_tiles(dep, leng, wid=None):
    if wid is None:
        wid = leng
    short_sides = 2 * wid * dep
    long_sides = 2 * leng * dep
    bottom = leng * wid
    total = short_sides + long_sides + bottom
    return total


def make_word(count):
    remainder = count % 10
    if count >= 11 and count <= 14:
        return "плиток"
    elif remainder == 1:
        return "плитка"
    elif remainder >= 2 and remainder <= 4:
        return "плитки"
    else:
        return "плиток"


total_tiles = count_tiles(2, 2, 2)
correct_word = make_word(total_tiles)
print('Потребуется', total_tiles, correct_word)
