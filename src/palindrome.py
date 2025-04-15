import string

def clean_text(text):
    allowed = string.ascii_letters + string.digits
    return ''.join(char.lower() for char in text if char.lower() in allowed)

def is_palindrome(text):
    cleaned = clean_text(text)
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    try:
        while True:
            entrada = input("Ingrese una palabra o frase: ")
            if is_palindrome(entrada):
                print(f'"{entrada}" es un palíndromo')
            else:
                print(f'"{entrada}" no es un palíndromo')
    except KeyboardInterrupt:
        print("\nPrograma finalizado.")
