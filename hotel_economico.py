from datetime import datetime
from collections import Counter

hoteis = [{
    'nome': 'Parque das Flores',
    'classificacao': 3,
    'regularSemana': 110,
    'regularFind': 90,
    'fielSemana': 80,
    'fielFind': 80
    },
    {
    'nome': 'Jardim Botânico',
    'classificacao': 4,
    'regularSemana': 160,
    'regularFind': 60,
    'fielSemana': 110,
    'fielFind': 50
    },
    {
    'nome': 'Mar Atlântico',
    'classificacao': 5,
    'regularSemana': 220,
    'regularFind': 150,
    'fielSemana': 100,
    'fielFind': 40
    }
]

def hotelMaisEconomico(string_de_entrada):
    string_de_entrada = string_de_entrada.split(': ')
    programa = string_de_entrada[0]
    datas = string_de_entrada[1].split(', ')
    hotel_valor_total = []

    for hotel in hoteis:
        valor = 0
        for data in datas:
            data = datetime.strptime(data, '%d/%m/%Y').date()
            if programa == 'Regular':
                if data.weekday() <= 4:
                    valor += hotel['regularSemana']
                else:
                    valor += hotel['regularFind']
            elif programa == 'Fidelidade':
                if data.weekday() <= 4:
                    valor += hotel['fielSemana']
                else:
                    valor += hotel['fielFind']

        hotel_valor_total.append({'nome': hotel['nome'],'classificacao':hotel['classificacao'],'valorTotalEstadia':valor})

    newlist = sorted(hotel_valor_total, key=lambda d: (d['valorTotalEstadia'],-d['classificacao'])) 
    return newlist[0]['nome']


input = input("Digite o tipo de programa de fidelidade seguido das datas: ")
print(hotelMaisEconomico(input))


     