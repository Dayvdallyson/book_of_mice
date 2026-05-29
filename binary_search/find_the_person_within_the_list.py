import unicodedata

people_in_the_list = [
    "Alice", "Allan", "Amanda", "Ana", "André", "Arthur",
    "Bárbara", "Beatriz", "Bernardo", "Bianca", "Breno", "Bruno",
    "Caio", "Camila", "Carla", "Carlos", "Carolina", "César",
    "Cíntia", "Clara", "Cristina",
    "Daniel", "Daniela", "Davi", "Débora", "Diego", "Douglas",
    "Eduardo", "Elaine", "Elisa", "Emanuel", "Érica",
    "Fabrício", "Fátima", "Felipe", "Fernanda",
    "Gabriel", "Gabriela", "Geovana", "Giovanna", "Gustavo",
    "Heitor", "Helena", "Henrique", "Hugo",
    "Igor", "Isabela", "Ivan",
    "Jaqueline", "Jefferson", "João", "Jonas", "Jorge", "José", "Júlia", "Juliana",
    "Karina", "Kelvin",
    "Larissa", "Laura", "Leonardo", "Letícia", "Lívia", "Lucas", "Luiza",
    "Marcelo", "Mariana", "Matheus", "Miguel", "Murilo",
    "Natasha", "Nathalia", "Nicolas",
    "Otávio",
    "Pablo", "Patrícia", "Paulo", "Pedro", "Priscila",
    "Rafael", "Rafaela", "Ramon", "Renato", "Ricardo", "Roberta", "Rodrigo",
    "Samuel", "Sandra", "Sérgio", "Sophia",
    "Tainá", "Thiago",
    "Valentina", "Vanessa", "Victor", "Vinicius", "Vitória",
    "William",
    "Yasmin", "Yuri"
]

def find_the_person_within_the_list(people_list, name):

    low = 0
    high = len(people_list) - 1


    while low <= high:

        mid = (low + high) // 2


        guess = unicodedata.normalize("NFKD",people_list[mid]).encode("ASCII", "ignore").decode("ASCII")


        if guess == unicodedata.normalize("NFKD",name).encode("ASCII", "ignore").decode("ASCII"):
            print("U FINALLY FOUNDED IT")

        if guess > unicodedata.normalize("NFKD",name).encode("ASCII", "ignore").decode("ASCII"):
            high = mid - 1

        else:
            low = mid + 1

    return None

find_the_person_within_the_list(people_in_the_list, "Bárbara")

# this case can generate a bug
print("á" > "z") # true
print("a" > "z") # false
