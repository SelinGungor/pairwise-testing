import pairwise.Pairwise as p


def generate(params):
    results = list(enumerate(p.pairwise(params)))
    return results


if __name__ == '__main__':
    testOracles = [
        ['iPhone 6S', 'iPhone 6S Plus', 'iPhone 7', 'iPad Air', 'iPad Pro 2'],
        ['iOS 9','iOS 10', 'iOS 11'],
        ['Chrome', 'Safari', 'Opera']
        ]
    outputData = generate(testOracles)
    with open('results.txt', 'w') as fH:
        for line in outputData:
            stringData = 'Pairwise {}:\t{}'.format(str(line[0]), str(line[1]))
            print(stringData)
            fH.write(stringData + '\n')