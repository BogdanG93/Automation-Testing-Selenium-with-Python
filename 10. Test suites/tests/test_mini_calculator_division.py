from app.mini_calculator import Mini_Calculator


class Test_Mini_Calc_Division:
    def setup_method(self):
        # start instructions
        self.calc = Mini_Calculator()

    def teardown_method(self):
        # final instructions
        pass

    def test_division(self):
        assert self.calc.division(6, 2) == 3
