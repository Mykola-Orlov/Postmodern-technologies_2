import unittest
import copy
from lab2 import SomeComponent, SelfReferencingEntity

class TestSomeComponent(unittest.TestCase):
    # перевіряємо, чи отримана копія є обєктом SomeComponent і чи зберігає вона ті ж значення атрибутів, що і оригінал
    def test_copy_method(self):
        original = SomeComponent(10, [1, 2, 3], SelfReferencingEntity())

        copied = copy.copy(original)

        self.assertIsInstance(copied, SomeComponent)
        self.assertEqual(copied.some_int, original.some_int)
        self.assertEqual(copied.some_list_of_objects, original.some_list_of_objects)
        self.assertIs(copied.some_circular_ref, original.some_circular_ref)

    # перевіряємо, чи отримана глибока копія також є обєктом SomeComponent, чи має вона ті ж значення атрибутів, що і оригінал
    # і чи створює вона новий об'єкт для атрибуту some_circular_ref
    def test_deepcopy_method(self):
        original = SomeComponent(20, [4, 5, 6], SelfReferencingEntity())

        deep_copied = copy.deepcopy(original)

        self.assertIsInstance(deep_copied, SomeComponent)
        self.assertEqual(deep_copied.some_int, original.some_int)
        self.assertEqual(deep_copied.some_list_of_objects, original.some_list_of_objects)
        self.assertIsNot(deep_copied.some_circular_ref, original.some_circular_ref)
        self.assertIsInstance(deep_copied.some_circular_ref, SelfReferencingEntity)

    # перевіряємо, чи новостворений об'єкт має очікувані значення для атрибутів some_int,
    # some_list_of_objects і some_circular_ref
    def test_init(self):
        some_int = 100
        some_list_of_objects = [1, 2, 3]
        some_circular_ref = SelfReferencingEntity()

        component = SomeComponent(some_int, some_list_of_objects, some_circular_ref)

        self.assertEqual(component.some_int, some_int)
        self.assertEqual(component.some_list_of_objects, some_list_of_objects)
        self.assertIs(component.some_circular_ref, some_circular_ref)


if __name__ == "__main__":
    unittest.main()