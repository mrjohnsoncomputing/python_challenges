# python_challenges
A collection of challenges produced by Mr Johnson which aim to get you to develop python applications to solve practical and engaging problems.

### Helper library
I would really recommend creating a file called `helper.py` when working through these challenges. This will be a python module where you include code that will help you in lots of different problems.

For example, you might include a definition for a function which reads files, such as:
```
def readfile(filename):
    # Code goes here
    # I'm not writing it for you
```

You can then use this in _other_ python files by importing this, like you would a library:
`import helper`

And then you can access any function definitions stored within like so:
`helper.readfile("diary.txt")`