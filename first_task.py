# Guido van Rossum <guido@python.org>
def step2_umbrella():
    print(
        'Утка-маляр 🦆 потеряла зонтик ☂️ и пошла в другой бар его искать. '
        'Утка-маляр 🦆 забыла зачем пришла и собралась уходить, '
        'на стойке около входа лежат зонтики ☂️, взять ей зонтик? ☂️'
        )
    option = ''
    options = {'да': 1, 'нет': 0, 'утка напилась': 2}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option] == 1:
        return step2_umbrella()
    elif options[option] == 0:
        return step2_no_umbrella()
    else:
        print('Утка напилась и забыла зачем пришла, она ушла домой 🏠')
        return


def step2_no_umbrella():
    print(
        'Утка-маляр 🦆 забыла, что не взяла зонтик ☂️ и пошла его искать '
        'в другой бар. '
        'Утка-маляр 🦆 забыла зачем пришла и собралась уходить,'
        'на стойке около входа лежат зонтики ☂️, '
        'взять ей зонтик? ☂️'
        )
    option = ''
    options = {'да': 1, 'нет': 0, 'утка напилась': 2}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option] == 1:
        return step2_umbrella()
    if options[option] == 0:
        return step2_no_umbrella()
    else:
        print('Утка напилась и забыла зачем пришла, она ушла домой 🏠')
        return


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
