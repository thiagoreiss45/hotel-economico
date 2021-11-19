from hotel_economico import hotelMaisEconomico

class TestClass:
    
    def test_one(self):
        assert hotelMaisEconomico('Regular: 16/03/2020, 17/03/2020, 18/03/2020') == 'Parque das Flores'

    def test_two(self):
        assert hotelMaisEconomico('Regular: 20/03/2020, 21/03/2020, 22/03/2020') == 'Jardim Botânico'

    def test_three(self):
        assert hotelMaisEconomico('Fidelidade: 26/03/2020, 27/03/2020, 28/03/2020') == 'Mar Atlântico'


    