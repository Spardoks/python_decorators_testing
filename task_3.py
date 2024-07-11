import types


from logger import logger


@logger(path='flat_generator.log')
def flat_generator(list_of_list):

    for elemnt in list_of_list:
        if isinstance(elemnt, list):
            for item in flat_generator(elemnt):
                yield item
        else:
            yield elemnt

def test_flat_generator_with_loger():

    list_of_lists = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists), types.GeneratorType)


if __name__ == '__main__':
    test_flat_generator_with_loger()
