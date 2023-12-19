import unittest
import app as tested_app
import json

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = tested_app.app.test_client()

    def test_get_hello_endpoint(self):
        r = self.app.get('/')        
        self.assertEqual(r._status_code, 200) 
        self.assertEqual(r.get_data(), b'Hello world from app Pipeline testing V2')    

if __name__ == '__main__':
    unittest.main()

'''import unittest
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
        self.assertEqual(self.order.view(), None)

    def test_view(self):
        orde = prog.OrderStack()
        orde.push('item1', 3)
        orde.push('item2', 5)

        expected_result = "Список замовлень:\n- item1 (3 одиниць)\n- item2 (5 одиниць)\n"
        self.assertEqual(orde.view(), expected_result)


if __name__ == "__main__":
    unittest.main()'''
