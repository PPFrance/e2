#Given an input text output it transposed.

### project setup

```
virtualenv -p python3 venv
source ./venv/bin/activate
pip install pytest
```

Roughly explained, the transpose of a matrix:
```
ABC
DEF
```
is given by:
```
AD
BE
CF
```
Rows become columns and columns become rows. See https://en.wikipedia.org/wiki/Transpose.

If the input has rows of different lengths, this is to be solved as follows:

##### - Pad to the left with spaces.
#####D - on't pad to the right.
Therefore, transposing this matrix:
```
ABC
DE
```
results in:
```
AD
BE
C
```
And transposing:
```
AB
DEF
```
results in:
```
AD
BE
 F
```
In general, all characters from the input should also be present in the transposed output. That means that if a column in the input text contains only spaces on its bottom-most row(s), the corresponding output row should contain the spaces in its right-most column(s).

#Exception messages
Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. Not every exercise will require you to raise an exception, but for those that do, the tests will only pass if you include a message.

To raise a message with an exception, just write it as an argument to the exception type. For example, instead of raise Exception, you should write:

raise Exception("Meaningful message indicating the source of the error")
Running the tests
To run the tests, run the appropriate command below (why they are different):
```
Python 2.7: py.test transpose_test.py
```
```
Python 3.4+: pytest transpose_test.py
```
Alternatively, you can tell Python to run the pytest module (allowing the same command to be used regardless of Python version): python -m pytest transpose_test.py

##Common pytest options
#####-v : enable verbose output
#####-x : stop running tests on first failure
#####--ff : run failures from previous test before running other test cases
For other options, see python -m pytest -h