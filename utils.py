def calcular_media(notas):
    """Calcula a média das notas"""
    return sum(notas) / len(notas)

def avaliar_aluno(media):
    """Avalia o aluno com base na média"""
    if media >= 5:
        return "Aprovado"
    else:
        return "Reprovado"

def ler_notas():
    """Lê as notas dos 4 bimestres"""
    notas = []
    for i in range(1, 5):
        while True:
            try:
                nota = float(input(f"Digite a nota do {i}º bimestre (0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota deve ser entre 0 e 10. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
    return notas

def verificar_easter_egg(notas):
    """Verifica se as notas correspondem à combinação secreta"""
    # Combinação ultra secreta 
    combinacao_secreta = [7, 7, 7, 7]
    
    if notas == combinacao_secreta:
        return "Oba tu achou um easter egg!!!11! 🎉 professor peloamordedeus não me reprova por isso"
    return ""
