          Height      Weight        Age  Grip strength    Frailty
count  10.000000   10.000000  10.000000      10.000000  10.000000
mean   68.600000  131.900000  32.500000      26.000000   0.400000
std     1.670662   14.231811  12.860361       4.521553   0.516398
min    65.800000  112.000000  17.000000      19.000000   0.000000
25%    67.825000  120.750000  22.250000      22.500000   0.000000
50%    68.450000  136.000000  29.500000      27.000000   0.000000
75%    69.700000  141.750000  43.500000      29.750000   1.000000
max    71.500000  153.000000  51.000000      31.000000   1.000000
Correlation Matrix:
                 Height    Weight       Age  Grip strength   Frailty
Height         1.000000  0.571525 -0.032580      -0.167682  0.193186
Weight         0.571525  1.000000  0.190926       0.032807  0.535200
Age           -0.032580  0.190926  1.000000       0.133756 -0.083655
Grip strength -0.167682  0.032807  0.133756       1.000000 -0.475867
Frailty        0.193186  0.535200 -0.083655      -0.475867  1.000000
Data Types:
Height           float64
Weight             int64
Age                int64
Grip strength      int64
Frailty            int64
dtype: object

Unique Values in Frailty Column:
[0 1]

Preprocessed Dataset:
   Height  Weight  Age  Grip strength  Frailty
0    65.8     112   30             30        0
1    71.5     136   19             31        0
2    69.4     153   45             29        0
3    68.2     142   22             28        1
4    67.8     144   29             24        1
5    68.7     123   50             26        0
6    69.8     141   51             22        1
7    70.1     136   23             20        1
8    67.9     112   17             19        0
9    66.8     120   39             31        0

T-Statistic: 1.5303334194571003
P-Value: 0.1644646461051128

Correlation Matrix:
                 Height    Weight       Age  Grip strength   Frailty
Height         1.000000  0.571525 -0.032580      -0.167682  0.193186
Weight         0.571525  1.000000  0.190926       0.032807  0.535200
Age           -0.032580  0.190926  1.000000       0.133756 -0.083655
Grip strength -0.167682  0.032807  0.133756       1.000000 -0.475867
Frailty        0.193186  0.535200 -0.083655      -0.475867  1.000000


Comparison of Grip Strength by Frailty Status:
T-Statistic: -1.5303334194571003
P-Value: 0.1644646461051128
Correlation coefficient between Grip strength and Frailty: -0.4758668672668007

Summary Statistics of Age by Frailty:
         count       mean        std   min    25%   50%   75%   max
Frailty                                                            
0          6.0  33.333333  13.633293  17.0  21.75  34.5  43.5  50.0
1          4.0  31.250000  13.524669  22.0  22.75  26.0  34.5  51.0



Optimization terminated successfully.
         Current function value: 0.554207
         Iterations 5
                           Logit Regression Results                           
==============================================================================
Dep. Variable:                Frailty   No. Observations:                   10
Model:                          Logit   Df Residuals:                        7
Method:                           MLE   Df Model:                            2
Date:                Sun, 11 Feb 2024   Pseudo R-squ.:                  0.1765
Time:                        04:53:24   Log-Likelihood:                -5.5421
converged:                       True   LL-Null:                       -6.7301
Covariance Type:            nonrobust   LLR p-value:                    0.3048
=================================================================================
                    coef    std err          z      P>|z|      [0.025      0.975]
---------------------------------------------------------------------------------
const             6.1553      4.904      1.255      0.209      -3.456      15.766
Age              -0.0029      0.059     -0.049      0.961      -0.119       0.113
Grip strength    -0.2518      0.182     -1.381      0.167      -0.609       0.106
=================================================================================
<Figure size 1000x600 with 0 Axes>