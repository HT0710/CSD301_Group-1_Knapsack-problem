
import sys
import os

from Algorithms.BranchAndBound import BranchAndBound
from Algorithms.BruteForce import BruteForce
from Algorithms.Genetic import Genetic
from .DynamicPrograming import DynamicPrograming
from .Greedy import GreedyProgram

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


DynamicPrograming = DynamicPrograming
GreedyProgram = GreedyProgram
BranchAndBound = BranchAndBound
BruteForce = BruteForce
Genetic = Genetic