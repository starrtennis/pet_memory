from django.test import TestCase
from pet_profile import PetPhoto

class PetPhotoTestCase(TestCase):
    def set_up(self):
        yield
    
    def test_sanity(self):
        self.assertEqual(1, 1)
    
    def test_doc_string(self):
        self.assertLessEqual(len(self.self), 255)