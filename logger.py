import datetime
import os


def logger(path):

    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(f'{time} {old_function.__name__}'
                               f' ({args}, {kwargs}) = {result}\n')
            return result

        return new_function

    return __logger
