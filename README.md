# AutoImpDiffPaths

## Brief Introduction

This program is an automatic four-round impossible differential path search for the ARIA algorithm, using the idea of ​​miss in the middle. 

## A Related Paper

The research paper detailing the automated path search program is available at [[https://github.com/rebound-rk/rebound-rk/blob/main/paper-quick-revised.pdf](https://github.com/whyaza/Automatically-find-impossible-differential-paths/blob/main/manuscript.pdf)](https://github.com/whyaza/Automatically-find-impossible-differential-paths/blob/main/manuscript.pdf). Within this paper, you will find a wealth of additional insights and explanations, encompassing various aspects:

**Validity Proof of Discovered Paths**: The paper rigorously verifies paths automatically identified by the program. 

**Multi-Round Attack Strategies**: The paper applies discovered paths to multi-round attacks. It discusses using these paths for intricate strategies spanning encryption rounds, contributing to the program's cryptanalysis potential.

**Comprehensive Complexity Analysis**: The paper extensively analyzes complexities. It covers classical and quantum perspectives, revealing efforts needed to breach security.

## Source Codes

Forward two-round paths (starting bytes with 2 non-zero values) are contained in forwardpropagation2.py.
Backward two-round paths (ending bytes with 8 non-zero values) are contained in backpropagation8.py.
Inputting 2 and 8 in Get_Impossible_Differential_Path.py will yield all the paths that have been automatically identified.
