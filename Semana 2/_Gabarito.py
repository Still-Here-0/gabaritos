import os
from time import sleep

def main(key_word:str) -> None:
    clear_terminal()
    list_wrong = []
    list_right = []
    max_vida = 6
    lower_key_word = key_word.lower()

    print('Bem vindo ao adivinhe a palavra!')
    
    while True:
        known_letters: str = set_view_lettes(key_word, lower_key_word, list_right)
        str_erros = get_erros_str(list_wrong)

        if known_letters == key_word:
            print(f'{key_word:^33}\nParabéns, você achou a palavra!!!')
            break
        elif len(list_wrong) >= max_vida:
            print(f'Infelizmente você perdeu...\nA palavra era "{key_word}"')
            break

        print(f'Você tem {max_vida - len(list_wrong)} vidas')
        gess: str = get_letter(known_letters, str_erros)


        if gess in list_right or gess in list_wrong:
            print('Você já escolheu essa letra')
        elif gess in lower_key_word:
            list_right.append(gess)
            print(f'Parabéns, "{gess}" está na palavra')
        else:
            list_wrong.append(gess)
            print(f'Infelizmente "{gess}" não está na palavra')
        
        sleep(1.5)
        clear_terminal()

def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def set_view_lettes(key_word:str, lower_key_word:str, right:list) -> str:
    known = ''
    for letter, lower_letter  in zip(key_word, lower_key_word):
        if lower_letter == ' ':
            known += ' '
        elif lower_letter in right:
            known += letter
        else:
            known += '_'
    
    return known

def get_letter(known_letters:str, wrong:str) -> str:
    print('Palavra chave:', known_letters)
    print('Erros:', wrong)
    gess: str = input('Escolha uma letra: ').lower()
    return gess

def get_erros_str(wrong:list) -> str:
        erros_str = ''
        for letter in wrong:
            erros_str += letter + ' - '
        return erros_str


if __name__ == "__main__":
    main('Bruno')
    pass