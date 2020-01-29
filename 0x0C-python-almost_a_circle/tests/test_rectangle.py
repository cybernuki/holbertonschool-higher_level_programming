#!/usr/bin/python3
# Author: Jhonatan Arenas <1164@holbertonschool.com>
# tests/test_rectangle.py
"""This module contains a test case class for Rectangle class

Sumary:

    Instantiation - verify if every in instantiation is correct ()
    Width_Validation - verify if the attribute width validates correctly ()
    height_Validation - verify if the attribute height validates correctly ()
    x_Validation - verify if the attribute x validates correctly ()
    y_Validation - verify if the attribute y validates correctly ()
    Area - Verify that the result of the area method is correct ()
"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_Instantiation(unittest.TestCase):
    """Test cases that verify if every in instantiation is correct"""

    @classmethod
    def setUpClass(self):
        print("\n[Start of Instantiation Test cases]")

    @classmethod
    def tearDownClass(self):
        print(" Done")

    def setUp(self):
        setattr(Rectangle, '_Base__nb_objects', 0)

    def test_instanceof(self):
        """verify if the object is an instance of the
        Rectangle and Base class"""
        r1 = Rectangle(10, 10)
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r1, Base)

    def test_arguments(self):
        """Verify scenarios when the init arguments are not correct"""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_id_system(self):
        """Test if the id system is working"""
        # We create 49 instances
        # So then, id must be equals to the i variable
        for i in range(1, 50):
            r = Rectangle(10, 10)
            self.assertEqual(r.id, i)
        # Also, at the end, id class attribute must be 49
        self.assertEqual(getattr(Rectangle, '_Base__nb_objects'), 49)
        # Now, we create 5 instances more, which has i variable as id
        for i in range(0, 10, 2):
            r = Rectangle(10, 10, 10, 10, i)
            self.assertEqual(r.id, i)
        # Finally, as we pass an id into the arguments, if we create a
        # new rectangle, it must has the id of 50
        r = Rectangle(10, 10)
        self.assertEqual(r.id, 50)

    def test_private_attributes(self):
        """Verify if the width, height, x and y attributes are private"""
        r = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r.__width
        with self.assertRaises(AttributeError):
            r.__height
        with self.assertRaises(AttributeError):
            r.__x
        with self.assertRaises(AttributeError):
            r.__y

    def test_setter_attributes(self):
        r = Rectangle(10, 20)
        r.width = 10
        r.height = 200
        r.x = 400
        r.y = 200

        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 200)
        self.assertEqual(r.x, 400)
        self.assertEqual(r.y, 200)

    def test_getters_attributes(self):
        """Verify if the getter methods works propertly"""
        r = Rectangle(10, 20)
        self.assertAlmostEqual(r.width, 10)
        self.assertAlmostEqual(r.height, 20)
        self.assertAlmostEqual(r.x, 0)
        self.assertAlmostEqual(r.y, 0)

        r = Rectangle(20, 10)
        self.assertAlmostEqual(r.width, 20)
        self.assertAlmostEqual(r.height, 10)
        self.assertAlmostEqual(r.x, 0)
        self.assertAlmostEqual(r.y, 0)
        self.assertAlmostEqual(r.id, 2)

        r = Rectangle(10, 20, 1, 2)
        self.assertAlmostEqual(r.width, 10)
        self.assertAlmostEqual(r.height, 20)
        self.assertAlmostEqual(r.x, 1)
        self.assertAlmostEqual(r.y, 2)

        r = Rectangle(10, 20, 2, 3)
        self.assertAlmostEqual(r.width, 10)
        self.assertAlmostEqual(r.height, 20)
        self.assertAlmostEqual(r.x, 2)
        self.assertAlmostEqual(r.y, 3)

        r = Rectangle(10, 20, 1, 2, 15)
        self.assertAlmostEqual(r.width, 10)
        self.assertAlmostEqual(r.height, 20)
        self.assertAlmostEqual(r.x, 1)
        self.assertAlmostEqual(r.y, 2)

        r = Rectangle(10, 20, 2, 3, 0)
        self.assertAlmostEqual(r.width, 10)
        self.assertAlmostEqual(r.height, 20)
        self.assertAlmostEqual(r.x, 2)
        self.assertAlmostEqual(r.y, 3)


class TestRectangle_Width_Validation(unittest.TestCase):
    """Test cases that verify if the attribute width validates correctly"""

    @classmethod
    def setUpClass(self):
        print("\n[Start of Width Validation Test cases]")

    @classmethod
    def tearDownClass(self):
        print(" Done")

    def setUp(self):
        setattr(Rectangle, '_Base__nb_objects', 0)

    def test_type_validation_str(self):
        """width is a string"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("hello", 10)

    def test_type_validation_double(self):
        """width is a double"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.4, 10)

    def test_type_validation_bool(self):
        """width is bool"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 10)

    def test_type_validation_None(self):
        """width is none"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 10)

    def test_type_validation_Nan(self):
        """width is none"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 10)

    def test_type_validation_object(self):
        """width is any object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(object, 10)

    def test_value_validation_negative(self):
        """width is a negative number"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 10)

    def test_value_validation_zero(self):
        """width is a zero"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 10)


class TestRectangle_height_Validation(unittest.TestCase):
    """Test cases that verify if the attribute width validates correctly"""

    @classmethod
    def setUpClass(self):
        print("\n[Start of height Validation Test cases]")

    @classmethod
    def tearDownClass(self):
        print(" Done")

    def setUp(self):
        setattr(Rectangle, '_Base__nb_objects', 0)

    def test_type_validation_str(self):
        """height is a string"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "Hello")

    def test_type_validation_double(self):
        """height is a double"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 10.4)

    def test_type_validation_bool(self):
        """height is bool"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, True)

    def test_type_validation_None(self):
        """height is none"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, None)

    def test_type_validation_Nan(self):
        """height is none"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, float('nan'))

    def test_type_validation_object(self):
        """height is any object"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, object)

    def test_value_validation_negative(self):
        """height is a negative number"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -10)

    def test_value_validation_zero(self):
        """height is a zero"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)


class TestRectangle_x_Validation(unittest.TestCase):
    """Test cases that verify if the attribute x validates correctly"""

    @classmethod
    def setUpClass(self):
        print("\n[Start of x Validation Test cases]")

    @classmethod
    def tearDownClass(self):
        print(" Done")

    def setUp(self):
        setattr(Rectangle, '_Base__nb_objects', 0)

    def test_type_validation_str(self):
        """x is a string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 10, "Hello")

    def test_type_validation_double(self):
        """x is a double"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 10, 10.4)

    def test_type_validation_bool(self):
        """x is bool"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, True)

    def test_type_validation_None(self):
        """x is none"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, None)

    def test_type_validation_Nan(self):
        """x is none"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 10, float('nan'))

    def test_type_validation_object(self):
        """x is any object"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 10, object)

    def test_value_validation_negative(self):
        """x is a negative number"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 10, -10)


class TestRectangle_y_Validation(unittest.TestCase):
    """Test cases that verify if the attribute y validates correctly"""

    @classmethod
    def setUpClass(self):
        print("\n[Start of y Validation Test cases]")

    @classmethod
    def tearDownClass(self):
        print("\tDone")

    def setUp(self):
        setattr(Rectangle, '_Base__nb_objects', 0)

    def test_type_validation_str(self):
        """y is a string"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 10, 10, "Hello")

    def test_type_validation_double(self):
        """y is a double"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 10, 10, 10.4)

    def test_type_validation_bool(self):
        """y is bool"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 10, True)

    def test_type_validation_None(self):
        """y is none"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 10, None)

    def test_type_validation_Nan(self):
        """y is none"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 10, 10, float('nan'))

    def test_type_validation_object(self):
        """y is any object"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 10, 10, object)

    def test_value_validation_negative(self):
        """y is a negative number"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 10, 10, -10)


class TestRectangle_Area(unittest.TestCase):
    """Verify that the result of the area method is correct"""

    @classmethod
    def setUpClass(self):
        print("\n[Start of area Test cases]")

    @classmethod
    def tearDownClass(self):
        print(" Done")

    def setUp(self):
        setattr(Rectangle, '_Base__nb_objects', 0)

    def test_correct_output(self):
        """Verify if the out put of the area method is correct"""
        r = Rectangle(10, 10)
        self.assertEqual(r.area(), 100)
        r = Rectangle(980000, 200000)
        self.assertEqual(r.area(), 196000000000)
        r = Rectangle(9821738912, 891273891)
        self.assertEqual(r.area(), 8753859456484346592)

    def test_output_after_changes(self):
        """Verify if the out put of the area method is correct
        after change the attributes
        """
        r = Rectangle(9821738912, 891273891)
        self.assertEqual(r.area(), 8753859456484346592)
        r.width = 10
        self.assertEqual(r.area(), 8912738910)
        r.height = 10
        self.assertEqual(r.area(), 100)

    def test_arguments(self):
        """Verify if the method raise a error when try to pass arguments"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 10)
            r.area(10)


class TestRectangle_Display(unittest.TestCase):
    """Verify that the result of the display method is correct"""

    @classmethod
    def setUpClass(self):
        print("\n[Start of dislay Test cases]")

    @classmethod
    def tearDownClass(self):
        print(" Done")

    def setUp(self):
        setattr(Rectangle, '_Base__nb_objects', 0)

    @staticmethod
    def get_stdout(obj, method):
        """captures the printed standar output"""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(obj)
        else:
            obj.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_no_padding_display(self):
        """Verify if the rectangle displays a normal grid"""
        r = Rectangle(3, 3)
        capture = TestRectangle_Display.get_stdout(r, "display")
        self.assertEqual("###\n###\n###\n", capture.getvalue())

    def test_x_padding_display(self):
        """Verify if the rectangle displays a normal grid with x padding"""
        r = Rectangle(3, 3, 2, 0)
        capture = TestRectangle_Display.get_stdout(r, "display")
        self.assertEqual("  ###\n  ###\n  ###\n", capture.getvalue())

    def test_y_padding_display(self):
        """Verify if the rectangle displays a normal grid with y padding"""
        r = Rectangle(3, 3, 0, 2)
        capture = TestRectangle_Display.get_stdout(r, "display")
        self.assertEqual("\n\n###\n###\n###\n", capture.getvalue())

    def test_xy_padding_display(self):
        """Verify if the rectangle displays a normal grid with y padding"""
        r = Rectangle(3, 3, 2, 2)
        capture = TestRectangle_Display.get_stdout(r, "display")
        self.assertEqual("\n\n  ###\n  ###\n  ###\n", capture.getvalue())


class TestRectangle_str(unittest.TestCase):
    """Verify that the result of the __str__ method is correct"""

    @classmethod
    def setUpClass(self):
        print("\n[Start of __str__ Test cases]")

    @classmethod
    def tearDownClass(self):
        print(" Done")

    def setUp(self):
        setattr(Rectangle, '_Base__nb_objects', 0)

    @staticmethod
    def get_stdout(obj, method):
        """captures the printed standar output"""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(obj)
        else:
            obj.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_print_method(self):
        """Test that print method use the correct __str__ format"""
        r = Rectangle(20, 10)
        capture = TestRectangle_str.get_stdout(r, "print")
        expected = "[Rectangle] ({}) 0/0 - 20/10\n".format(r.id)
        self.assertEqual(expected, capture.getvalue())

    def test_str_method_height_width_x(self):
        """Evaluates that the instance.__str__() methods returns
        the correct output"""
        r = Rectangle(40, 50, 10)
        expected = "[Rectangle] ({}) 10/0 - 40/50".format(r.id)
        self.assertEqual(expected, r.__str__())

    def test_str_method_height_width_x_y(self):
        """Evaluates that the str() methods prints
        the correct output"""
        r = Rectangle(100, 20, 10, 20)
        expected = "[Rectangle] ({}) 10/20 - 100/20".format(r.id)
        self.assertEqual(expected, str(r))

    def test_str_method_height_width_x_y_id(self):
        """Evaluates that the str() methods prints
        the correct output"""
        r = Rectangle(100, 20, 10, 20, 99)
        expected = "[Rectangle] (99) 10/20 - 100/20"
        self.assertEqual(expected, str(r))

    def test_str_method_changed_attributes(self):
        """Evaluates that the str() methods prints
        the correct output"""
        r = Rectangle(100, 20, 10, 20, 99)
        r.width = 1
        r.height = 2
        r.x = 3
        r.y = 4
        expected = "[Rectangle] (99) 3/4 - 1/2"
        self.assertEqual(expected, str(r))


class TestRectangle_update(unittest.TestCase):
    """Verify that the result of the update method is correct"""

    @classmethod
    def setUpClass(self):
        print("\n[Start of update Test cases]")

    @classmethod
    def tearDownClass(self):
        print(" Done")

    def setUp(self):
        setattr(Rectangle, '_Base__nb_objects', 0)

    def test_args_zero_args(self):
        """Verify if args update is working with zero args"""
        r = Rectangle(33, 33, 33, 33)
        r.update()
        self.assertEqual("[Rectangle] ({}) 33/33 - 33/33".format(r.id), str(r))

    def test_args_one_args(self):
        """Verify if args update is working one args"""
        r = Rectangle(33, 33, 33, 33)
        r.update(10)
        self.assertEqual("[Rectangle] (10) 33/33 - 33/33", str(r))

    def test_args_two_args(self):
        """Verify if args update is working one args"""
        r = Rectangle(33, 33, 33, 33)
        r.update(10, 20)
        self.assertEqual("[Rectangle] (10) 33/33 - 20/33", str(r))

    def test_args_three_args(self):
        """Verify if args update is working two args"""
        r = Rectangle(33, 33, 33, 33)
        r.update(10, 20, 30)
        self.assertEqual("[Rectangle] (10) 33/33 - 20/30", str(r))

    def test_args_four_args(self):
        """Verify if args update is working two args"""
        r = Rectangle(33, 33, 33, 33)
        r.update(10, 20, 30, 40)
        self.assertEqual("[Rectangle] (10) 40/33 - 20/30", str(r))

    def test_args_five_args(self):
        """Verify if args update is working two args"""
        r = Rectangle(33, 33, 33, 33)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual("[Rectangle] (10) 40/50 - 20/30", str(r))

    def test_args_five_more_args(self):
        """Verify if args update is working two args"""
        r = Rectangle(33, 33, 33, 33)
        r.update(10, 20, 30, 40, 50, 100)
        self.assertEqual("[Rectangle] (10) 40/50 - 20/30", str(r))

    def test_args_twice_operation(self):
        """Verify if update changes whit a double call"""
        r = Rectangle(33, 33, 33, 33)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual("[Rectangle] (10) 40/50 - 20/30", str(r))
        r.update(89, 102, 103, 104, 107)
        self.assertEqual("[Rectangle] (89) 104/107 - 102/103", str(r))

    def test_args_wrong_type_values(self):
        """Verify if update changes whit a double call"""
        r = Rectangle(33, 33, 33, 33)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, "20")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(10, 20, "30")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(10, 20, 30, "40")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(10, 20, 30, 40, "50")

    def test_args_wrong_values(self):
        """Verify if update changes whit a double call"""
        r = Rectangle(33, 33, 33, 33)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(10, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(10, -10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(10, 20, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(10, 20, -10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(10, 20, 30, -10)
        r.update(10, 20, 30, 0)
        self.assertEqual("[Rectangle] (10) 0/33 - 20/30", str(r))
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(10, 20, 30, 10, -10)
        r.update(10, 20, 30, 0, 0)
        self.assertEqual("[Rectangle] (10) 0/0 - 20/30", str(r))

    def test_kwargs_one_args(self):
        """Verify if kwargs update is working with zero args"""
        r = Rectangle(33, 33, 33, 33)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 33/33 - 33/33", str(r))

    def test_kwargs_two_args(self):
        """Verify if kwargs update is working with two args"""
        r = Rectangle(33, 33, 33, 33)
        r.update(id=1, width=2)
        self.assertEqual("[Rectangle] (1) 33/33 - 2/33", str(r))

    def test_kwargs_three_args(self):
        """Verify if kwargs update is working with three args"""
        r = Rectangle(33, 33, 33, 33)
        r.update(id=1, width=2, height=3)
        self.assertEqual("[Rectangle] (1) 33/33 - 2/3", str(r))

    def test_kwargs_four_args(self):
        """Verify if kwargs update is working with four args"""
        r = Rectangle(33, 33, 33, 33)
        r.update(id=1, width=2, height=3, x=4)
        self.assertEqual("[Rectangle] (1) 4/33 - 2/3", str(r))

    def test_kwargs_five_args(self):
        """Verify if kwargs update is working with five args"""
        r = Rectangle(33, 33, 33, 33)
        r.update(id=1, width=2, height=3, x=4, y=5)
        self.assertEqual("[Rectangle] (1) 4/5 - 2/3", str(r))

    def test_id_None(self):
        """Verify if kwargs update has id as None"""
        r = Rectangle(33, 33, 33, 33)
        r.update(id=None)
        self.assertEqual("[Rectangle] ({}) 33/33 - 33/33".format(r.id), str(r))
        r.update(id=None, width=2, height=3, x=4, y=5)
        self.assertEqual("[Rectangle] ({}) 4/5 - 2/3".format(r.id), str(r))

    def test_invalid_type(self):
        """Verify if kwargs update has invalid type values"""
        r = Rectangle(33, 33, 33, 33)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width=None)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height=None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x=None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y=None)

    def test_invalid_value(self):
        """Verify if kwargs update has invalid values"""
        r = Rectangle(33, 33, 33, 33)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-10)

    def test_kwargs_args(self):
        """Verify if kwargs update is working with five args and kwargs"""
        r = Rectangle(33, 33, 33, 33)
        r.update(89, 10, height=3, x=4, y=5)
        self.assertEqual("[Rectangle] (89) 33/33 - 10/33", str(r))

    def test_wrong_key(self):
        """Verify if kwargs update is working with five args and kwargs"""
        r = Rectangle(33, 33, 33, 33)
        r.update(a=3, b=4, c=5)
        self.assertEqual("[Rectangle] ({}) 33/33 - 33/33".format(r.id), str(r))
        r.update(width=3, height=4, c=5)
        self.assertEqual("[Rectangle] ({}) 33/33 - 3/4".format(r.id), str(r))


if __name__ == "__main__":
    unittest.main()
