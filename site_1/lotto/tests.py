from django.test import TestCase
from lotto.models import GuessNumbers

class GuessNumbersTestCase(TestCase):
   def test_generate(self):
    g = GuessNumbers(name='Test numbers', text='selected numbers')
    g.generate()
    
    print(g.update_date)
    print(g.lottos)

    # default로 6개 숫자 x 5 set = 30개의 숫자가 생성됨을 확인
    self.assertTrue(len(g.lottos) > 20) # (OK or FAILED)