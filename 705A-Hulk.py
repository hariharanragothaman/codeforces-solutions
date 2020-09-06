def hulk(n):
    odd_end = "I hate it"
    even_end = " I love it"
    if n == 1:
        return odd_end

    output = ''
    i = 0
    str = 'hate'
    prev = None
    while i < n:
        if prev == 'hate':
            str = 'love'
        else:
            str = 'hate'
        output += ' I ' + str + ' that'
        prev = str
        i += 1

    return output


if __name__ == '__main__':
    n = int(input())
    output = hulk(n).lstrip()
    output = output.split()
    output[-1] = 'it'
    output = ' '.join(c for c in output)
    print(output)

"""
expected: 'I hate that I love that I hate that I love it'
found   : 'I hate that I love that I hate it'
"""
