import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import unittest
from marathon import solution

class TestMarathone(unittest.TestCase):
  def test_solution1(self):
    participant = 	["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    expect_result = 'leo'
    result = solution(participant, completion)
    self.assertEqual(result, expect_result)
    print('[TEST CASE 1]')
    print('participant: [' + ','.join(str(man) for man in participant) + ']')
    print('completion: [' + ','.join(str(man) for man in completion) + ']')
    print('expect: %s, receive: %s, result: %r\n' %(expect_result, result, expect_result == result) )
  
  def test_solution2(self):
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    expect_result = 'mislav'
    result = solution(participant, completion)
    self.assertEqual(result, expect_result)
    print('[TEST CASE 2]')
    print('participant: [' + ','.join(str(man) for man in participant) + ']')
    print('completion: [' + ','.join(str(man) for man in completion) + ']')
    print('expect: %s, receive: %s, result: %r\n' %(expect_result, result, expect_result == result) )

if __name__ == '__main__':
  unittest.main()