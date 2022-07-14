def find_in(iterable, finerd, expected):
    for i in iterable:
        if finerd(i) == expected:
            return
    raise NotFoundError(f'{expected} not found in provided iterable.')


class NotFoundError(Exception):
    pass


if __name__ == "__main__":
    print(find_in(['Jenna', 'Lindsey', 'Thai'], lambda x: x, 'Jenna'))
