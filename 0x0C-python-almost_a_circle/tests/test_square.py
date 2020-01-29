#!/usr/bin/python3
# Author: Jhonatan Arenas <1164@holbertonschool.com>
# tests/test_square.py
"""This module contains a test case class for Square class

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
from models.square import Square


class TestRectangle_Instantiation(unittest.TestCase):
    """Test cases that verify if every in instantiation is correct"""

    @classmethod
    def setUpClass(self):
        print("\n------------\n Square test cases:\n------------\n")
        print("\n[Start of Instantiation Test cases]")

    @classmethod
    def tearDownClass(self):
        print(" Done")

    def setUp(self):
        setattr(Square, '_Base__nb_objects', 0)

    def test_instanceof(self):
        """verify if the object is an instance of the
        Rectangle and Base class"""
        sq = Square(10)
        self.assertIsInstance(sq, Square)
        self.assertIsInstance(sq, Rectangle)
        self.assertIsInstance(sq, Base)

    def test_arguments(self):
        """Verify scenarios when the init arguments are not correct"""
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_id_system(self):
        """Test if the id system is working"""
        # We create 49 instances
        # So then, id must be equals to the i variable
        for i in range(1, 50):
            sq = Square(10)
            self.assertEqual(sq.id, i)
        # Also, at the end, id class attribute must be 49
        self.assertEqual(getattr(Square, '_Base__nb_objects'), 49)
        # Now, we create 5 instances more, which has i variable as id
        for i in range(0, 10, 2):
            sq = Square(10, 10, 10, i)
            self.assertEqual(sq.id, i)
        # Finally, as we pass an id into the arguments, if we create a
        # new rectangle, it must has the id of 50
        sq = Square(10)
        self.assertEqual(sq.id, 50)

    def test_private_attributes(self):
        """Verify if the width, height, x and y attributes are private"""
        sq = Square(1)
        with self.assertRaises(AttributeError):
            sq.__width
        with self.assertRaises(AttributeError):
            sq.__height
        with self.assertRaises(AttributeError):
            sq.__x
        with self.assertRaises(AttributeError):
            sq.__y

    def test_setter_attributes(self):
        sq = Square(20)
        sq.width = 10
        sq.height = 200
        sq.x = 400
        sq.y = 200

        self.assertEqual(sq.width, 10)
        self.assertEqual(sq.height, 200)
        self.assertEqual(sq.x, 400)
        self.assertEqual(sq.y, 200)

        sq.size = 10
        self.assertAlmostEqual(sq.size, sq.width)
        self.assertAlmostEqual(sq.size, sq.height)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.size = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.size = -10
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.size = "hola"
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.size = 1.5
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.size = True
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.size = None
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.size = object

    def test_getters_attributes(self):
        """Verify if the getter methods works propertly"""
        sq = Square(20)
        self.assertAlmostEqual(sq.width, 20)
        self.assertAlmostEqual(sq.size, sq.width)
        self.assertAlmostEqual(sq.size, sq.height)
        self.assertAlmostEqual(sq.x, 0)
        self.assertAlmostEqual(sq.y, 0)

        sq = Square(20, 1, 2)
        self.assertAlmostEqual(sq.width, 20)
        self.assertAlmostEqual(sq.size, sq.width)
        self.assertAlmostEqual(sq.size, sq.height)
        self.assertAlmostEqual(sq.x, 1)
        self.assertAlmostEqual(sq.y, 2)

        sq = Square(20, 2, 3)
        self.assertAlmostEqual(sq.width, 20)
        self.assertAlmostEqual(sq.size, sq.width)
        self.assertAlmostEqual(sq.size, sq.height)
        self.assertAlmostEqual(sq.x, 2)
        self.assertAlmostEqual(sq.y, 3)

        sq = Square(20, 1, 2, 15)
        self.assertAlmostEqual(sq.width, 20)
        self.assertAlmostEqual(sq.size, sq.width)
        self.assertAlmostEqual(sq.size, sq.height)
        self.assertAlmostEqual(sq.x, 1)
        self.assertAlmostEqual(sq.y, 2)

        sq = Square(20, 2, 3, 0)
        self.assertAlmostEqual(sq.width, 20)
        self.assertAlmostEqual(sq.size, sq.width)
        self.assertAlmostEqual(sq.size, sq.height)
        self.assertAlmostEqual(sq.x, 2)
        self.assertAlmostEqual(sq.y, 3)
        


class TestRectangle_size_Validation(unittest.TestCase):
    """Test cases that verify if the parameter size  is correctly validated"""

    @classmethod
    def setUpClass(self):
        print("\n[Start of size Validation Test cases]")

    @classmethod
    def tearDownClass(self):
        print(" Done")

    def setUp(self):
        setattr(Square, '_Base__nb_objects', 0)

    def test_type_validation_str(self):
        """Size is a string"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("Hello")

    def test_type_validation_double(self):
        """Size is a double"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(10.4)

    def test_type_validation_bool(self):
        """Size is bool"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_type_validation_None(self):
        """Size is none"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_type_validation_Nan(self):
        """Size is nan"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_type_validation_object(self):
        """Size is any object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(object)

    def test_value_validation_negative(self):
        """Size is a negative number"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-10)

    def test_value_validation_zero(self):
        """Size is a zero"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)


class TestRectangle_x_Validation(unittest.TestCase):
    """Test cases that verify if the attribute x validates correctly"""

    @classmethod
    def setUpClass(self):
        print("\n[Start of x Validation Test cases]")

    @classmethod
    def tearDownClass(self):
        print(" Done")

    def setUp(self):
        setattr(Square, '_Base__nb_objects', 0)

    def test_type_validation_str(self):
        """x is a string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, "Hello")

    def test_type_validation_double(self):
        """x is a double"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, 10.4)

    def test_type_validation_bool(self):
        """x is bool"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, True)

    def test_type_validation_None(self):
        """x is none"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, None)

    def test_type_validation_Nan(self):
        """x is none"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, float('nan'))

    def test_type_validation_object(self):
        """x is any object"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, object)

    def test_value_validation_negative(self):
        """x is a negative number"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -10)


class TestRectangle_y_Validation(unittest.TestCase):
    """Test cases that verify if the attribute y validates correctly"""

    @classmethod
    def setUpClass(self):
        print("\n[Start of y Validation Test cases]")

    @classmethod
    def tearDownClass(self):
        print("\tDone")

    def setUp(self):
        setattr(Square, '_Base__nb_objects', 0)

    def test_type_validation_str(self):
        """y is a string"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 10, "Hello")

    def test_type_validation_double(self):
        """y is a double"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 10, 10.4)

    def test_type_validation_bool(self):
        """y is bool"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 10, True)

    def test_type_validation_None(self):
        """y is none"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 10, None)

    def test_type_validation_Nan(self):
        """y is none"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 10, float('nan'))

    def test_type_validation_object(self):
        """y is any object"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 10, object)

    def test_value_validation_negative(self):
        """y is a negative number"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 10, -10)


class TestRectangle_Area(unittest.TestCase):
    """Verify that the result of the area method is correct"""

    @classmethod
    def setUpClass(self):
        print("\n[Start of area Test cases]")

    @classmethod
    def tearDownClass(self):
        print(" Done")

    def setUp(self):
        setattr(Square, '_Base__nb_objects', 0)

    def test_correct_output(self):
        """Verify if the out put of the area method is correct"""
        sq = Square(10)
        self.assertEqual(sq.area(), 100)
        sq = Square(200000)
        self.assertEqual(sq.area(), (200000 * 200000))
        sq = Square(891273891)
        self.assertEqual(sq.area(), (891273891 * 891273891))

    def test_output_after_changes(self):
        """Verify if the out put of the area method is correct
        after change the attributes
        """
        sq = Square(891273891)
        self.assertEqual(sq.area(), (891273891 * 891273891))
        sq.width = 10
        self.assertEqual(sq.area(), 8912738910)
        sq.height = 10
        self.assertEqual(sq.area(), 100)

    def test_arguments(self):
        """Verify if the method raise a error when try to pass arguments"""
        with self.assertRaises(TypeError):
            sq = Square(10)
            sq.area(10)


class TestRectangle_Display(unittest.TestCase):
    """Verify that the result of the display method is correct"""

    @classmethod
    def setUpClass(self):
        print("\n[Start of dislay Test cases]")

    @classmethod
    def tearDownClass(self):
        print(" Done")

    def setUp(self):
        setattr(Square, '_Base__nb_objects', 0)

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
        sq = Square(3)
        capture = TestRectangle_Display.get_stdout(sq, "display")
        self.assertEqual("###\n###\n###\n", capture.getvalue())

    def test_x_padding_display(self):
        """Verify if the rectangle displays a normal grid with x padding"""
        sq = Square(3, 2, 0)
        capture = TestRectangle_Display.get_stdout(sq, "display")
        self.assertEqual("  ###\n  ###\n  ###\n", capture.getvalue())

    def test_y_padding_display(self):
        """Verify if the rectangle displays a normal grid with y padding"""
        sq = Square(3, 0, 2)
        capture = TestRectangle_Display.get_stdout(sq, "display")
        self.assertEqual("\n\n###\n###\n###\n", capture.getvalue())

    def test_xy_padding_display(self):
        """Verify if the rectangle displays a normal grid with y padding"""
        sq = Square(3, 2, 2)
        capture = TestRectangle_Display.get_stdout(sq, "display")
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
        setattr(Square, '_Base__nb_objects', 0)

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
        sq = Square(20)
        capture = TestRectangle_str.get_stdout(sq, "print")
        expected = "[Square] ({}) 0/0 - 20\n".format(sq.id)
        self.assertEqual(expected, capture.getvalue())

    def test_str_method_height_width_x(self):
        """Evaluates that the instance.__str__() methods returns
        the correct output"""
        sq = Square(40, 10)
        expected = "[Square] ({}) 10/0 - 40".format(sq.id)
        self.assertEqual(expected, sq.__str__())

    def test_str_method_height_width_x_y(self):
        """Evaluates that the str() methods prints
        the correct output"""
        sq = Square(100, 10, 20)
        expected = "[Square] ({}) 10/20 - 100".format(sq.id)
        self.assertEqual(expected, str(sq))

    def test_str_method_height_width_x_y_id(self):
        """Evaluates that the str() methods prints
        the correct output"""
        sq = Square(100, 10, 20, 99)
        expected = "[Square] (99) 10/20 - 100"
        self.assertEqual(expected, str(sq))

    def test_str_method_changed_attributes(self):
        """Evaluates that the str() methods prints
        the correct output"""
        sq = Square(100, 10, 20, 99)
        sq.width = 1
        sq.height = 2
        sq.x = 3
        sq.y = 4
        expected = "[Square] (99) 3/4 - 1"
        self.assertEqual(expected, str(sq))


class TestRectangle_update(unittest.TestCase):
    """Verify that the result of the update method is correct"""

    @classmethod
    def setUpClass(self):
        print("\n[Start of update Test cases]")

    @classmethod
    def tearDownClass(self):
        print(" Done")

    def setUp(self):
        setattr(Square, '_Base__nb_objects', 0)

    def test_args_zero_args(self):
        """Verify if args update is working with zero args"""
        sq = Square(33, 33, 33)
        sq.update()
        self.assertEqual("[Square] ({}) 33/33 - 33".format(sq.id), str(sq))

    def test_args_one_args(self):
        """Verify if args update is working one args"""
        sq = Square(33, 33, 33)
        sq.update(10)
        self.assertEqual("[Square] (10) 33/33 - 33", str(sq))

    def test_args_two_args(self):
        """Verify if args update is working one args"""
        sq = Square(33, 33, 33)
        sq.update(10, 20)
        self.assertEqual("[Square] (10) 33/33 - 20", str(sq))

    def test_args_three_args(self):
        """Verify if args update is working two args"""
        sq = Square(33, 33, 33)
        sq.update(10, 20, 30)
        self.assertEqual("[Square] (10) 30/33 - 20", str(sq))

    def test_args_four_args(self):
        """Verify if args update is working two args"""
        sq = Square(33, 33, 33)
        sq.update(10, 20, 30, 40)
        self.assertEqual("[Square] (10) 30/40 - 20", str(sq))

    def test_args_five_args(self):
        """Verify if args update is working two args"""
        sq = Square(33, 33, 33)
        sq.update(10, 20, 30, 40, 50)
        self.assertEqual("[Square] (10) 30/40 - 20", str(sq))

    def test_args_twice_operation(self):
        """Verify if update changes whit a double call"""
        sq = Square(33, 33, 33)
        sq.update(10, 20, 30, 40)
        self.assertEqual("[Square] (10) 30/40 - 20", str(sq))
        sq.update(89, 102, 103, 104)
        self.assertEqual("[Square] (89) 103/104 - 102", str(sq))

    def test_args_wrong_type_values(self):
        """Verify if update changes whit a double call"""
        sq = Square(33, 33, 33)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(10, "20")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(10, 20, "40")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.update(10, 20, 40, "50")

    def test_args_wrong_values(self):
        """Verify if update changes whit a double call"""
        sq = Square(33, 33, 33, 33)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(10, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(10, -10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq.update(10, 20, -10)
        sq.update(10, 20, 0)
        self.assertEqual("[Square] (10) 0/33 - 20", str(sq))
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq.update(10, 20, 30, -10)
        sq.update(10, 20, 0, 0)
        self.assertEqual("[Square] (10) 0/0 - 20", str(sq))

    def test_kwargs_one_args(self):
        """Verify if kwargs update is working with zero args"""
        sq = Square(33, 33, 33)
        sq.update(id=1)
        self.assertEqual("[Square] (1) 33/33 - 33", str(sq))

    def test_kwargs_two_args(self):
        """Verify if kwargs update is working with two args"""
        sq = Square(33, 33, 33)
        sq.update(id=1, width=2)
        self.assertEqual("[Square] (1) 33/33 - 33", str(sq))

    def test_kwargs_three_args(self):
        """Verify if kwargs update is working with three args"""
        sq = Square(33, 33, 33)
        sq.update(id=1, width=2, height=3)
        self.assertEqual("[Square] (1) 33/33 - 33", str(sq))

    def test_kwargs_size_args(self):
        """Verify if kwargs update is working with size args"""
        sq = Square(33, 33, 33)
        sq.update(id=1, width=2, height=3, size=100)
        self.assertEqual("[Square] (1) 33/33 - 100", str(sq))

    def test_kwargs_four_args(self):
        """Verify if kwargs update is working with four args"""
        sq = Square(33, 33, 33)
        sq.update(id=1, width=2, height=3, size=100, x=4)
        self.assertEqual("[Square] (1) 4/33 - 100", str(sq))

    def test_kwargs_five_args(self):
        """Verify if kwargs update is working with five args"""
        sq = Square(33, 33, 33)
        sq.update(id=1, width=2, height=3, x=4, y=5, size=100)
        self.assertEqual("[Square] (1) 4/5 - 100", str(sq))

    def test_id_None(self):
        """Verify if kwargs update has id as None"""
        sq = Square(33, 33, 33)
        sq.update(id=None)
        self.assertEqual("[Square] ({}) 33/33 - 33".format(sq.id), str(sq))
        sq.update(id=None, width=2, height=3, x=4, y=5, size=100)
        self.assertEqual("[Square] ({}) 4/5 - 100".format(sq.id), str(sq))

    def test_invalid_type(self):
        """Verify if kwargs update has invalid type values"""
        sq = Square(33, 33, 33)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(size=None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(x=None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.update(y=None)

    def test_invalid_value(self):
        """Verify if kwargs update has invalid values"""
        sq = Square(33, 33, 33)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(size=0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(size=-10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq.update(x=-10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq.update(y=-10)

    def test_kwargs_args(self):
        """Verify if kwargs update is working with five args and kwargs"""
        sq = Square(33, 33, 33)
        sq.update(89, 10, size=3, x=4, y=5)
        self.assertEqual("[Square] (89) 33/33 - 10", str(sq))

    def test_wrong_key(self):
        """Verify if kwargs update is working with five args and kwargs"""
        sq = Square(33, 33, 33)
        sq.update(a=3, b=4, c=5)
        self.assertEqual("[Square] ({}) 33/33 - 33".format(sq.id), str(sq))
        sq.update(size=3, c=5)
        self.assertEqual("[Square] ({}) 33/33 - 3".format(sq.id), str(sq))


class TestRectangle_dict(unittest.TestCase):
    """Verify that the result of the to_dict method is correct"""

    @classmethod
    def setUpClass(self):
        print("\n[Start of to_dict Test cases]")

    @classmethod
    def tearDownClass(self):
        print(" Done")

    def setUp(self):
        setattr(Square, '_Base__nb_objects', 0)

    def test_to_dictionary_output(self):
        sq = Square(10, 2, 9, 5)
        correct = {'x': 2, 'y': 9, 'id': 5, 'size': 10}
        self.assertDictEqual(correct, sq.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        sq1 = Square(10, 2, 9, 5)
        sq2 = Square(5, 9, 1, 10)
        sq2.update(**sq1.to_dictionary())
        self.assertNotEqual(sq1, sq2)

    def test_to_dictionary_arg(self):
        sq = Square(10, 2, 1, 2)
        with self.assertRaises(TypeError):
            sq.to_dictionary(1)
