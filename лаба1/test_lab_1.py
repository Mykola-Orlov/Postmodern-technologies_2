import sys
import unittest
from io import StringIO
from lab_1 import reverse_string

class TestReverseString(unittest.TestCase):
    
    def test_check(self):
        with self.assertRaises(SystemExit) as cm: 
            reverse_string("hello") 
            self.assertEqual(cm.exception.code, 0)

        with self.assertRaises(SystemExit) as cm: 
            reverse_string("123") 
            self.assertEqual(cm.exception.code, 0)
        
        with self.assertRaises(SystemExit) as cm: 
            reverse_string(5) 
            self.assertEqual(cm.exception.code, 1)
    
    def test_reverse_string(self):
        input_str = "123"  # вводимо значення в stdin
        sys.stdin = StringIO(input_str)
        original_stdout = sys.stdout # зберігаємо початковий потік stdout
        fake_stdout = StringIO() # створюємо новий об'єкт StringIO для перехоплення stdout
        sys.stdout = fake_stdout
        expected_output = "321" # очікуваний вивід (stdout)
        try:                           # запуск функції
            reverse_string(input_str)
        except SystemExit:
            pass              # виходимо з програми, бо sys.exit(0) викликає SystemExit
        sys.stdout = original_stdout  # повертаємо потіе stdout до його початкового значення
        actual_output = fake_stdout.getvalue() # отримуємо актуальний вивід
        self.assertEqual(actual_output, expected_output) # перевірка очікуваного і фактуального виводу

    def test_error_handling(self):
        input_data = 123  # передаємо некоректні дані
        expected_error_message = "Error: 'int' object is not subscriptable"
        stderr_backup = sys.stderr
        sys.stderr = StringIO() # заміна sys.stderr на об'єкт StringIO для зберігання вмісту
        with self.assertRaises(SystemExit) as cm:  # викликаємо функцію з некоректними даними
            reverse_string(input_data)
        self.assertEqual(cm.exception.code, 1)
        actual_error_message = sys.stderr.getvalue().strip() # отримуємо вміст, записаний у stderr
        sys.stderr = stderr_backup # повертаємо sys.stderr до оригінального стану
        self.assertEqual(actual_error_message, expected_error_message) # перевіряємо, чи виведено очікуване повідомлення про помилку у stderr

if __name__ == "__main__":
    unittest.main()