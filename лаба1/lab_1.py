import sys
import unittest
from io import StringIO

# функція приймає рядок і виводить його оберненим, + якщо праграма виконалася успішно повертається "0", якщо помилка то "1"
def reverse_string(input_str):
    try:
        reversed_str = input_str[::-1]
        print(reversed_str)
        return 0
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        return 1
    

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        input_data = "hello" # вхід
        expected_output = "olleh" # очікуваний вивід
        with StringIO() as stdout:  # перенаправляємо вивід на stdout
            with StringIO() as stderr:  # перенаправляємо вивід на stderr
                sys.stdout = stdout
                sys.stderr = stderr
                self.assertEqual(reverse_string(input_data), 0) # викликаємо функцію і очікуємо результат "0"(програма успішно виконалася)
                self.assertEqual(stdout.getvalue().strip(), expected_output) # перевіряємо чи вивід співпадає з очікуваним результатом
                self.assertEqual(stderr.getvalue(), "") # перевіряємо чи є stderr порожній

    def test_reverse_string_error(self):
        input_data = 123  # вхід (не рядок)
        with StringIO() as stdout:
            with StringIO() as stderr:
                sys.stdout = stdout
                sys.stderr = stderr
                self.assertEqual(reverse_string(input_data), 1) # викликаємо функцію і очікуємо результат "1"(Error)
                self.assertEqual(stdout.getvalue(), "")
                self.assertNotEqual(stderr.getvalue(), "")  # перевіряємо чи є щось в stderr, а не порожній рядок


if __name__ == "__main__":
    unittest.main()
    