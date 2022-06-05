import os

def main():
    veiw = 0
    path_contacts = os.path.dirname(__file__) + "\Contatos.txt"
    initialize_contacts_file(path_contacts)
    contacts:dict = txt_to_dict(path_contacts)

    while True:
        clear_tetminal()

        match veiw:
            case 0:
                veiw = veiw_menu()
            case 1:
                veiw = veiw_set_contacts(path_contacts)
            case 2:
                veiw = veiw_find_name(path_contacts)
            case 3:
                veiw = veiw_check_number(path_contacts)
            case 4:
                veiw = veiw_delete(path_contacts)
            case 5:
                break

def initialize_contacts_file(path:str) -> None:
    with open(path, 'a', encoding='UTF-8') as file:
        pass

def clear_tetminal() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

def txt_to_dict(csv_path:str) -> dict:
    """Vou assumir que o arquivo txt de contatos está formatado no estilo csv (comma separated values)
    """
    with open(csv_path, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        dict_contacts = dict()
        for line in lines:
            num, name = line.split(',')
            dict_contacts[num] = name[:-1]
    
    return dict_contacts

def veiw_menu() -> int:
    print(
        'Bem vindo a lista telefônica feita pelo Bruno',
        'Escolha uma das opções a baixo',
        '1 - Inserir um contato',
        '2 - Procurar por um nome',
        '3 - Checar um número',
        '4 - Deletar um contato',
        '5 - Sair da lista telefônica',
        '',
        sep='\n'
    )
    try:
        choice = int(input('Escolha uma das opções: '))
        if choice > 5 or choice < 1:
            raise ValueError
    except ValueError:
        choice = 0
        input('Escolha umas das opções "1", "2", "3", "4" ou "5"')

    return choice

def veiw_set_contacts(path:str):
    print('Para voltar ao menu escreva "menu()"')
    name = get_name()
    if name == 'menu()':
        return 0
    
    num = get_num()
    if num == 'menu()':
        return 0

    dict_contacts = txt_to_dict(path)

    if num in dict_contacts.keys():
        choise = input(
            f'Esse número já pertence a uma pessoa ({dict_contacts[num]})\n' +\
            f'Deseja sobre escrever o nome associado ao número (s/n)?\n'
        )
        if choise != 's':
            input('Voltando ao menu')
            return 0
        else:
            change_contact(path, num, name)
    else:
        set_new_contact(path, num, name)

    input('Contato inserido com sucesso')
    return 0

def get_name() -> str:
    while True:
        name = input(f'Nome do contato:   ')
        if ',' in name:
            print('Nomes não podem ter virgulas ","')
        else:
            break
    
    return name

def get_num() -> str:
    while True:
        num = input(f'Número do contato: ')
        if num.isnumeric():
            break
        else:
            print('Você não digitou um número')

    return num

def change_contact(path:str, setter_num:str, set_name:str):
    with open(path, 'r+', encoding='UTF-8') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            num, name = line.split(',')
            if num == setter_num:
                line = f'{setter_num},{set_name}\n'
            file.write(line)

def set_new_contact(path:str, num:str, name:str):
    with open(path, 'a', encoding='UTF-8') as file:
        file.write(f'{num},{name}\n')

def veiw_find_name(path) -> int:
    dict_contacts = txt_to_dict(path)
    if len(dict_contacts) == 0:
        input(
            'Infelizmente você ainda não possui contatos\n'
            'Aperte "enter" volte para o menu e insira conatos'
        )
        return 0
    
    veiw_names(dict_contacts)
    
    return 0

def veiw_names(contacts:dict) -> bool:
    name_filter = ''
    while name_filter != 'menu()':
        for num in contacts:
            if name_filter in contacts[num] or name_filter == '':
                print(f'{contacts[num]:<18}{"->":^6}{num:<18}')
        name_filter = input('Deseja filtra a lista de contatos?\nOBS: Digite "menu()" para voltar ao menu\n')
        clear_tetminal()

def veiw_check_number(path:str) -> int:
    test_num = input('Qual número você quer procurar? ')
    dict_cotacts = txt_to_dict(path)
    if test_num in dict_cotacts.keys():
        input(f'O número {test_num} pertence a {dict_cotacts[test_num]}')
    else:
        input(f'O número {test_num} não está na sua listade contatos')
    
    return 0

def veiw_delete(path:str) -> int:
        delet_num = input('Qual número você deseja deletar da sua lista telefônica: ')
        dict_contacts = txt_to_dict(path)

        try:
            del(dict_contacts[delet_num])
        except KeyError:
            print(f'Você não possui o número {delet_num} na sua lista telefônica')
        else:
            delete_txt(path, dict_contacts)
        finally:
            input('Ação concluida voltanado ao menu')
        
        return 0

def delete_txt(path:str, dict_:dict) -> None:
    with open(path, 'w', encoding='UTF-8') as file:
        for key in dict_:
            file.write(f'{key},{dict_[key]}\n')
    

if __name__ == "__main__":
    main()