
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from .DynamicPrograming import DynamicPrograming
from .Greedy import GreedyProgram
from .Backtrack import Backtrack


DynamicPrograming = DynamicPrograming
GreedyProgram = GreedyProgram
Backtrack = Backtrack