# Variables are also called identifier names

# ⭐ first_name -> Normal convention

# ⭐ _name -> Indicates that is a private or for internal use: Objects named this way will not get imported by
# from module import *

# ⭐ __age -> Used to "mangle" class attributes - useful in inhetitance chains

# ⭐ __calc__ -> User defined dunder methods that have a special meaning to the interpreter
# 🔥 Dont invent them. Stick to the ones provided by Python!

"""
Examples:

__init__

num1 < num2 --> num1.__lt__(num2)


"""

"""
Other Naming Conventions            From PEP 8 Style Guide

Packages                            utilities
Modules                             db_utils, dbutils
Classes                             BankAccount
Functions                           open_account
Variables                           account_id
Constants                           MIN_INTEREST


https://peps.python.org/pep-0008/

A Foolish Consistency is the Hobgoblin of Little Minds - Emerson

"""
