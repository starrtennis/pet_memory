from django.test import TestCase

class SanityTestCase(TestCase):
    def setUp(self):
        yield #no set up for a sanity test!
        
    def test_boolean_logic(self):
        self.assertEqual(True, True)
        self.assertEqual(False, False)
        self.assertEqual(False, True) #test short circuits here on failure; how to test all invalid assertions?
        self.assertEqual(True, False)
        
        self.assertTrue(True)
        self.assertTrue(False)
        self.assertFalse(False)
        self.assertFalse(True)
        
    #look at Django class TransactionTestCase.