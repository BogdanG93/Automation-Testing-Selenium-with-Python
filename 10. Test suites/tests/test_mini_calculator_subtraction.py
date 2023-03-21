from app.mini_calculator import Mini_Calculator


class Test_Mini_Calc_Subtraction:
    def setup_method(self):
        # start instructions
        self.calc = Mini_Calculator()

    def teardown_method(self):
        # final instructions
        pass

    def test_subtraction(self):
        assert self.calc.substraction(8, 4) == 4
