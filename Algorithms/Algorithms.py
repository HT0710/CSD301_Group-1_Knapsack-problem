
import sys
import os

from Algorithms.BranchAndBound import BranchAndBound
from Algorithms.BruteForce import BruteForce
from Algorithms.BruteForceMemorization import BruteForceMemorization
from Algorithms.MeetInTheMiddle import MeetInTheMiddle
from .DynamicPrograming import DynamicPrograming
from .Greedy import GreedyProgram

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Define some algorithm classes
DynamicPrograming = DynamicPrograming
GreedyProgram = GreedyProgram
BranchAndBound = BranchAndBound
BruteForceMemorization = BruteForceMemorization
BruteForce = BruteForce
MeetInTheMiddle = MeetInTheMiddle