from utils import calcular_media, avaliar_aluno, ler_notas, verificar_easter_egg

def main():
    # Solicita o nome do aluno
    nome = input("Digite o nome do aluno: ").strip()
    
    # Valida se o nome não está vazio
    while not nome:
        print("Nome não pode estar vazio. Tente novamente.")
        nome = input("Digite o nome do aluno: ").strip()
    
    # Lê as notas do aluno
    notas = ler_notas()
    
    # Calcula a média das notas
    media = calcular_media(notas)
    
    # Avalia o aluno com base na média
    status = avaliar_aluno(media)
    
    # Verifica se há um easter egg
    easter_egg_msg = verificar_easter_egg(notas)
    
    # Exibe o resultado
    print("\n" + "="*30)
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")
    if easter_egg_msg:
        print(f"\n{easter_egg_msg}")
    print("="*30)

if __name__ == "__main__":
    main()


# to passano mal