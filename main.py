from os import close

from kolejka import Kolejka

if __name__ == '__main__':
    kolejka = Kolejka()
    print(f'Witamy w kinie Jedynka \n')
    print(input(f'Wpisz swoje imie i nazwisko: '))

    print(f'Aktualnie w kolejce: \n')
    kolejka.show()

    kolejka.show_places()


    close()