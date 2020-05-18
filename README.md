# NAtural DAte Ranges

The purposed of this package is to translate natural language phrases describing date ranges into relevant dates or strings.

# Installation

`pip install nadar`

# How to use the package

`import nadar as nd`

**parse_reference**
Takes in a string representing a delta in date and returns it given the reference date.

```
>>> nd.parse_reference('today')
SmartDate(2020-05-18)
```

# Acknowledgment

The main author of the code for this package is [**Benjamin Wolter, PhD**](https://www.linkedin.com/in/benjamin-wolter/).