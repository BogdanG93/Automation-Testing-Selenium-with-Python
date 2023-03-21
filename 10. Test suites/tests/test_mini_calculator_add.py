from app.mini_calculator import Mini_Calculator


class Test_Mini_Calc_Sum:
    def setup_method(self):
        # start instructions
        self.calc = Mini_Calculator()

    def teardown_method(self):
        # final instructions
        pass

    def test_add_numbers(self):
        assert self.calc.add_numbers(10, 15) == 25
