def oxford_comma(items):
    if len(items) == 1:
        return ''.join(items)

    if len(items) > 1 and len(items) < 3:
        return ' and '.join(items)

    if len(items) > 2:
        phrase = []
        last = ', and ' + (items.pop(-1))
        ' '.join(last)

        oxford = ', '.join(items)

        phrase.append(oxford)
        phrase.append(last)

        return ''.join(phrase)

    
