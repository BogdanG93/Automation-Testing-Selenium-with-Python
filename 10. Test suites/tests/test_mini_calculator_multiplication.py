from app.mini_calculator import Mini_Calculator


class Test_Mini_Calc_Multiplication:
    def setup_method(self):
        # start instructions
        self.calc = Mini_Calculator()

    def teardown_method(self):
        # final instructions
        pass

    def test_multiplication(self):
        assert self.calc.multiplication(3, 4) == 12
