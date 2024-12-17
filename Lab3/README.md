# Lab 3: Unit Testing

## Objectives

- Write unit tests to test a function.
- Run unit tests and interpret the results.

---

## Tasks

### Task 1: Set-up
- Clone the repository containing the lab artifacts.
- Navigate to the directory with the exercise files.

### Task 2: Write Unit Tests
- Create a new Python file named `test_mymodule.py`.
- Write unit tests to test the functions in `mymodule.py`.
  ```python
  import unittest
  from mymodule import add, square, double
  
  class TestAdd(unittest.TestCase):
      def test_add(self):
          self.assertEqual(add(2, 4), 6)
          self.assertEqual(add(0, 0), 0)
          self.assertEqual(add(2.3, 3.6), 5.9)
          self.assertEqual(add('hello', 'world'), 'helloworld')
          self.assertNotEqual(add(-2, -2), 0)
  
  class TestSquare(unittest.TestCase):
      def test_square(self):
          self.assertEqual(square(2), 4)
          self.assertEqual(square(3.0), 9.0)
          self.assertNotEqual(square(-3), -9)
  
  class TestDouble(unittest.TestCase):
      def test_double(self):
          self.assertEqual(double(2), 4)
          self.assertEqual(double(-3.1), -6.2)
          self.assertEqual(double(0), 0)
  
  if __name__ == '__main__':
      unittest.main()
