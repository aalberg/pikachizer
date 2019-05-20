# Pikachizer

A recreation of [http://pikachizer.eye-of-newt.com/](http://pikachizer.eye-of-newt.com/)

## Usage

```shell
pikachizer.py <input_file> <output_file>
```

All upper and lower-case English letters are converted to Pikachu language. Numbers, symbols, and non-English characters are left untouched.

## Implementation Differences

This implementation of the Pikachizer does not look for bold or italic text to "excite" the output text.

There are also several small differences in the way random numbers are consumed; the algorithm used [here](http://pikachizer.eye-of-newt.com/) was not fully reverse engineered.
