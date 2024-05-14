# Installation

## Installation guide

To install `TreePy` use 

```
pip install treepy
```

## Quickstart

Then to use we can write

```py hl_lines="5-7"
from treepy.abilities import BaseTree

t = BaseTree('Oak')

def my_function(t: BaseTree):

    t.print_name()
```