import sys
import unittest
from io import StringIO

# функція приймає рядок і виводить його оберненим, + якщо програма виконалася успішно повертається "0", якщо помилка то "1"
def reverse_string(input_str):
    try:
        reversed_str = input_str[::-1]
        print(reversed_str)
        return 0
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        return 1
    

class TestReverseString(unittest.TestCase):
    # метод де створюємо об'єкти StringIO для перенаправлення stdout та stderr
    def setUp(self):
        self.stdout = StringIO()  # створюємо об'єкт StringIO для перенаправлення stdout
        self.stderr = StringIO()  #          - || -                               stderr
        sys.stdout = self.stdout  # перенаправляємо stdout на об'єкт StringIO
        sys.stderr = self.stderr  #    - || -       stderr    - || -

    # метод де повертаємо stdout та stderr до їх оригінальних станів
    def tearDown(self):
        sys.stdout = sys.__stdout__  # повертаємо stdout до його оригінального стану
        sys.stderr = sys.__stderr__  # повертаємо stderr     - || -
    
    # метод де перевіряємо, чи виведений текст у stdout відповідає результату
    def test_reverse_string_stdout(self):
        input_data = "hello"
        expected_output = "olleh"
        reverse_string(input_data)
        self.assertEqual(self.stdout.getvalue().strip(), expected_output) # отримуємо весь вміст, який був направлений у stdout, + видаляємо пробіли, + зрівнюємо результат який вийшов з очікуваним
    
    # метод де перевіряємо, чи виведений текст у stderr не є порожнім рядком
    def test_reverse_string_stderr(self):
        input_data = 123
        reverse_string(input_data)
        self.assertNotEqual(self.stderr.getvalue().strip(), "")
    
    # метод де перевіряємо, чи повертається коректний код виходу у випадку успішного виконання функції
    def test_reverse_string_success_exit_code(self):
        input_data = "hello"
        exit_code = reverse_string(input_data)
        self.assertEqual(exit_code, 0)
    
    # метод де перевіряємо, чи повертається коректний код виходу у випадку помилки під час виконання функції
    def test_reverse_string_error_exit_code(self):
        input_data = 123
        exit_code = reverse_string(input_data)
        self.assertEqual(exit_code, 1)


if __name__ == "__main__":
    if len(sys.argv) == 1:  # якщо аргументів командного рядка немає
        input_data = sys.stdin.readline().strip()  # зчитуємо вхідні дані з консолі
        reverse_string(input_data)  # викликаємо функцію обробки рядка
    else:
        unittest.main()  # запускаємо тести