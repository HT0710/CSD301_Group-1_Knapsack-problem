
import sys
import os

from Algorithms.BranchAndBound import BranchAndBound
from Algorithms.BruteForce import BruteForce
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from .DynamicPrograming import DynamicPrograming
from .Greedy import GreedyProgram
from .Backtrack import Backtrack


DynamicPrograming = DynamicPrograming
GreedyProgram = GreedyProgram
Backtrack = Backtrack
BranchAndBound = BranchAndBound
BruteForce = BruteForce