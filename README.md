# Ampify engineering placement test

Contents: This repository contains my solutions for the Ampify technical assessment.

Name: Sophie Kirkup

IDE used: Visual Studio Code


***

## C++ Calculator

For the C++ task I used the MinGW-w64 compiler, and ran a Build using g++ to create the executable file.


### Changes made

I first added `#include <cassert>` in the include list as it was missing, so that the assertions in the Result Checker could be carried out. I also fixed a bug in the unit tests: 2 - 5.6 = -2.6 (not 2.6).

I then added division to the calculator by including 'division' or '/' wherever add (+), substract (-) and multiply (*) were throughout the code.

I also added pi. My solution is in the Tokeniser class - it checks the input for any instance of 'pi' and replaces it with '3.14159". Initially I tried using `#define _USE_MATH_DEFINES` along with `#include <cmath>` at the start of the source code so that I could use the variable M_PI, which has the value of pi. However, with my solution, the `replace()` function required the input to be a string (value of M_PI is not a string) so I decided to keep it simple by hard coding in the value of pi.

I finally added set the precision of the outputs in the Calculator class using `cout.precision(7)`. This ensures that pi * 5 is calculated to five decimal places.


### Running the software
I have provided a calculator.exe file which can be run.


***

## Web API Parsing

Packages used:
* `urllib` - for handling the given url
* `json` - for parsing the JSON data so that the data read can be handled as a Python dictionary

I created 2 functions, `sortGenres` and `findHipHopPacks`. Both make use of iteration to append useful data to arrays which are then outputted to the user upon running. 

### Running the software (windows)

1. Use cd to locate the directory which contains the `parser.py` file in the command-line (cmd)
2. Enter `parser.py` 