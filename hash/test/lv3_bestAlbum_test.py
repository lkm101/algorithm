import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import unittest
from lv3_bestAlbum import solution

class TestBestAlbum(unittest.TestCase):
  def test_solution1(self):
    params1 = ["classic", "pop", "classic", "classic", "pop"]
    params2 = [500, 600, 150, 800, 2500]
    expect = [4, 1, 3, 0]
    result = solution(params1, params2)
    print('Input > %s, %s' %(params1, params2))
    print('Expect > %s' %(expect))
    self.assertEqual(result, expect)
    print('Rsult: %s\n' %('SUCCESS' if expect == result else 'FAILED'))
  
  def test_solution2(self):
    params1 = ["kpop", "kpop", "idol", "kpop", "jpop", "classic", "classic", "pop"]
    params2 = [500, 600, 150, 800, 50, 300, 120, 600]
    expect = [3, 1, 7, 5, 6, 2, 4]
    result = solution(params1, params2)
    print('Input > %s, %s' %(params1, params2))
    print('Expect > %s' %(expect))
    self.assertEqual(result, expect)
    print('Rsult: %s\n' %('SUCCESS' if expect == result else 'FAILED'))

if __name__ == '__main__':
  unittest.main()