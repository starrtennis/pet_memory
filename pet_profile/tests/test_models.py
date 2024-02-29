from django.test import TestCase
from pet_profile.models import PetPhoto

class GeneralTestCase(TestCase):
    def test_sanity_1(self):
        self.assertEqual(1, 1)
    
    def test_sanity_2(self):
        self.assertEqual(0,0)
        
    def test_sanity_3(self):
        self.assertLess(0,1)
        
    def test_sanity_4(self):
        self.assertGreater(1,0)

class PetPhotoTestCase(TestCase):
    p_ph = PetPhoto()
    
    def get_docstring_1(self):
        return self.p_ph
        
    def get_docstring_2(self):
        return self.p_ph.__str__()
        
    def get_docstring_3(self):
        return self.p_ph.title
    
    def test_doc_string(self):
        self.assertNotEqual(self.get_docstring_1(), self.get_docstring_2()) #object != docstring of object
        self.assertNotEqual(self.get_docstring_1(), self.get_docstring_3()) #object != "title" field of of object
        self.assertEqual(self.get_docstring_2(), self.get_docstring_3())    #docstring of object == "title" field of object
        self.assertEqual(self.get_docstring_1(), self.get_docstring_1())    # self-check (calibrator) #1
        self.assertEqual(self.get_docstring_2(), self.get_docstring_2())    # self-check (calibrator) #2
        self.assertEqual(self.get_docstring_3(), self.get_docstring_3())    # self-check (calibrator) #3