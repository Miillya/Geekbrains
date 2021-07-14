# Задание №2
# Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def grow_huffman_tree(s):
    chars_from_s = list(sorted(Counter(s).items(), key=lambda item: item[1]))

    while len(chars_from_s) > 1:
        weight = chars_from_s[0][1] + chars_from_s[1][1]
        node = MyNode(left=chars_from_s.pop(0)[0], right=chars_from_s.pop(0)[0])

        for i, item in enumerate(chars_from_s):
            if weight > item[1]:
                continue
            else:
                chars_from_s.insert(i, (node, weight))
                break
        else:
            chars_from_s.append((node, weight))

    return chars_from_s[0][0]


def huffman_encode(tree, code, path=''):
    if isinstance(tree, MyNode):
        huffman_encode(tree.left, code, path=path + '0')
        huffman_encode(tree.right, code, path=path + '1')
    else:
        code[tree] = path


str_ = input('Введите строку: ')

encoded = dict()
huffman_encode(grow_huffman_tree(str_), encoded)

print(*[encoded[char] for char in str_])
