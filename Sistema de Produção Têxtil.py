def obter_tipo_roupa():
    while True:
        tipo = input("Escolha o tipo de roupa (camiseta, calça, casaco) ou 'sair' para finalizar: ").lower()
        if tipo in ['camiseta', 'calça', 'casaco', 'sair']:
            return tipo
        else:
            print("Tipo de roupa inválido. As opções são: camiseta, calça ou casaco.")

def obter_tamanho_roupa():
    while True:
        tamanho = input("Escolha o tamanho da roupa (P, M, G): ").upper()
        if tamanho in ['P', 'M', 'G']:
            return tamanho
        else:
            print("Tamanho inválido. As opções são: P, M ou G.")

def obter_quantidade():
    while True:
        try:
            quantidade = int(input("Informe a quantidade de peças: "))
            if quantidade > 0:
                return quantidade
            else:
                print("A quantidade deve ser um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def calcular_preco(tipo, tamanho, quantidade):
    precos = {
        'camiseta': {'P': 20, 'M': 25, 'G': 30},
        'calça': {'P': 40, 'M': 45, 'G': 50},
        'casaco': {'P': 70, 'M': 80, 'G': 90}
    }
    return precos[tipo][tamanho] * quantidade

def main():
    print("Bem-vindo ao Sistema de Produção de Roupas!")
    while True:
        tipo_roupa = obter_tipo_roupa()
        if tipo_roupa == 'sair':
            print("Obrigado por utilizar o sistema!")
            break

        tamanho_roupa = obter_tamanho_roupa()
        quantidade = obter_quantidade()

        preco_total = calcular_preco(tipo_roupa, tamanho_roupa, quantidade)
        print(f"O valor total da produção de {quantidade} {tipo_roupa}(s) tamanho {tamanho_roupa} é: R${preco_total:.2f}\n")

if __name__ == "__main__":
    main()
