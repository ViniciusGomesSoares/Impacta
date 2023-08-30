'''
1. Classe Animal:
- Atributos:
- `nome`: Representa o nome do animal (por exemplo, "Rex").
- `tipo`: Define a classificação do animal (como "Mamífero", "Réptil", etc.).
- `som`: Descreve o som característico que o animal faz (como "Latido", "Miado", etc.).
- Construtor:
- Inicializa os atributos `nome`, `tipo`, e `som`.
- Métodos:
- `setSom(String som)`: Permite alterar o som do animal.
- `fazerSom()`: Imprime a ação de o animal fazer o seu som característico.
- `alimentar()`: Imprime a ação de alimentar o animal.
- `dormir()`: Imprime a ação do animal dormindo.
- `mostrarInfo()`: Imprime as informações do animal.
'''

class Animal:
    def __init__(self, nome, tipo, som):
        self.nome = nome
        self.tipo = tipo
        self.som = som

    def setSom(self, som):
        self.som = som

    def getSom(self):
        return self.som
    
    def setSom(self, nome):
        self.nome = nome

    def getSom(self):
        return self.nome
    
    def fazerSom(self):
        print(f"O animal {self.nome} faz o som {self.som}!!")
    
    def alimentar(self):
        print("Animal alimentado!!")
    
    def dormir(self):
        print("Animal dormindo!!")

    def mostrarInfo(self):
        print(f"Nome: {self.nome}")
        print(f"Tipo: {self.tipo}")
        print(f"Som: {self.som}")

def main():
    animal1 = Animal("Rodolpho","porco","roinc")
    animal2 = Animal("Tico","gato","miau")
    animal3 = Animal("Rex","cao","auau")

    animal1.mostrarInfo()
    animal1.setSom("SomNovo: muuuuu")
    print(animal1.getSom())

    animal3.fazerSom()

    animal2.mostrarInfo()
    animal2.alimentar()

    animal3.mostrarInfo()
    animal3.dormir()

if __name__=="__main__":
    main()