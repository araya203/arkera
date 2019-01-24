import unittest


def highest_possible_loss(n):
    if not n:
        return 0

    hi = n[0]
    low = n[0]
    hpl = 0
   
    for num in n:
        if num > hi:
            hi = num
        if num < hi:
            low = num
            hpl = min(hpl, num - hi)
    return hpl


class TestHPL(unittest.TestCase):

    #General tests
    def test_highest_possible_loss(self):
        self.assertEqual(highest_possible_loss([10,30,42,11,70,55,100,2,120,1,30,0,900]), -120)
        self.assertEqual(highest_possible_loss([10,30,42,11,70,55,100,2,120,1,30,0,900]), -120)
        self.assertEqual(highest_possible_loss([10,20,30,40,50,60,70,80,90,100]), 0)
        self.assertEqual(highest_possible_loss([100,90,80,70,60,50,40,30,20,10,1]), -99)


    #If the input list is empty
    def test_highest_possible_loss_if_list_empty(self):
        self.assertEqual(highest_possible_loss([]),0)


    #If the input list has negative values
    def test_highest_possible_loss_if_negative_values(self):
        self.assertEqual(highest_possible_loss([-100,-90,-80,-70,-60,-50,-40,-30,-20,-10,-1]),0 )
        self.assertEqual(highest_possible_loss([-1,-10,-20,-30,-40,-50,-60,-70,-80,-90,-100]),-99 )


    #If the input list has only one value
    def test_highest_possible_loss_if_only_one_value(self):
        self.assertEqual(highest_possible_loss([10]),0 )
        self.assertEqual(highest_possible_loss([0]),0 )
    
    
    #If the input list has only two values
    def test_highest_possible_loss_if_only_two_value(self):
        self.assertEqual(highest_possible_loss([10, 30]),0 )
        self.assertEqual(highest_possible_loss([50, 30]),-20)

    def test_highest_possible_loss_if_input_not_list(self):
        self.assertRaises(TypeError, highest_possible_loss, 3)

    def test_highest_possible_loss_if_input_is_string(self):
        self.assertRaises(TypeError, highest_possible_loss, "hello")

def main():
    unittest.main()


if __name__ == '__main__':
    main() 
