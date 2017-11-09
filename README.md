[![Build Status](https://travis-ci.org/mfuentesg/luhnpy.svg?branch=master)](https://travis-ci.org/mfuentesg/luhnpy)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://raw.githubusercontent.com/mfuentesg/luhnpy/master/LICENSE.md)
[![luhnpy release](https://img.shields.io/github/release/mfuentesg/luhnpy.svg)](https://img.shields.io/github/release/mfuentesg/luhnpy.svg?maxAge=2592000)


# Luhnpy


Luhnpy is a  [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm) implementation written in Python.  


### Installation
  
```
pip install luhnpy
```

### Examples


```python
import luhnpy

# Create random valid luhn strings
print(luhnpy.rand()) # 4124796630572739
print(luhnpy.rand(length=5)) # 41285
print(luhnpy.rand(length=10)) # 4380357030

# Calculate luhn check digit
print(luhnpy.digit('412479663057273')) # 9

# Verify string of digits
print(luhnpy.verify('4124796630572739')) # True
print(luhnpy.verify('4039531371114851')) # False

#  Append the check digit to your string of digits
print(luhnpy.complete('412479663057273')) # 4124796630572739
```
