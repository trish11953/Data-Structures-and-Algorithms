import homework1_tvm5513
import unittest


class testing_123(unittest.TestCase):

    def test_get_polynomial(self):
        p = homework1_tvm5513.Polynomial([(2, 1), (1, 0)])
        print(p.get_polynomial())

    def test_neg(self):
        p = homework1_tvm5513.Polynomial([(2, 1), (1, 0)])
        q = -p
        print(q.get_polynomial())

   # def test_simplify(self):
  #      p = homework1_tvm5513.Polynomial([(2, 1), (1, 0)])
  #      q = -p + (p * p)
   #     print(q.get_polynomial())
   #     q = q.simplify()
   #     print(q.get_polynomial())

    def test_str(self):
        p = homework1_tvm5513.Polynomial([(1, 1), (1, 0)])
        qs = (p, p + p, -p, -p - p, p * p)
        for q in qs:
            q.simplify()
        print(str(q))


if __name__ == '__main__':
    unittest.main()
