import sys
from datetime import date
from unittest import TestCase
sys.path.append('.')
from classes.taskclass import Task

class TestTaskClass(TestCase):

    def test_create_task(self):
        mytask = Task("Buy Groserries",["Milk", "Eggs","Tomato", "Coffe"], date.today())
        print(f" Mi tareea {mytask.tittle}")
