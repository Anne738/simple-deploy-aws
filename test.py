import unittest
import prog

class TestOrderStack(unittest.TestCase):
    def setUp(self):
        self.order = prog.OrderStack()
  
    def test_add1(self):
        self.assertEqual(self.order.push("kk", 2), None)

    def test_add2(self):
        self.assertFalse(self.order.push("",0))

    def test_addexept(self):
        with self.assertRaises(TypeError):
            self.order.push()

    def test_pop1(self):
        self.order.push("", 3)
        self.assertEqual(self.order.pop(), None)

    def test_popexept(self):
        orde = prog.OrderStack()
        with self.assertRaises(IndexError):
            orde.pop()

    def test_view(self):
        orde = prog.OrderStack()
        orde.push('item1', 3)
        orde.push('item2', 5)

        expected_result = "Список замовлень:\n- item1 (3 одиниць)\n- item2 (5 одиниць)\n"
        self.assertEqual(orde.view(), expected_result)


if __name__ == "__main__":
    unittest.main()
