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
    def init_PetPhoto(self):
        p_ph = PetPhoto()
        return p_ph
    
    def get_docstring_1(self):
        p_ph = init_PetPhoto(self)
        return p_ph
        
    def get_docstring_2(self):
        p_ph = init_PetPhoto(self)
        return p_ph.__str__(self)
        
    def get_docstring_3(self):
        p_ph = init_PetPhoto(self)
        return p_ph.title
    
    def test_doc_string(self):
        self.assertEqual(get_docstring_1(self), get_docstring_2(self))
        self.assertEqual(get_docstring_1(self), get_docstring_3(self))
        self.assertEqual(get_docstring_2(self), get_docstring_3(self))
        self.assertEqual(get_docstring_1(self), get_docstring_1(self))
        self.assertEqual(get_docstring_2(self), get_docstring_2(self))
        self.assertEqual(get_docstring_3(self), get_docstring_3(self))