# The CryoSat Community Processor

### Welcome

The CryoSat Community Processor is a project that offers a processor for CryoSat-2 data that anyone can use. The difference between this and other processors is that it is not just public, but also fully documented.

Community contributions are not just accepted, but encouraged. However all contributions must be fully documented using numpy docstrings and a detailed pull request. Published code is not useful unless it can be used! 

### Coding style

All contributed code *should* conform to [PEP 8](https://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds). This may seem intimidating if you've never read PEP 8, but you're probably doing most of it already.

All contributed code *should* also use [numpy docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html). This is a specific format of docstrings that can be compiled automatically to produce documentation. Most code editors offer an autofilling function for this! 

All contributed code *should* include tests. This is because CCP makes use of continuous integration using Travis. This means that with each push to the github repo, tests are run automatically to check that you haven't broken the code.

Finally, contributed code *must* be functional, not object orientated. If you don't know what a class is, then ignore this. This choice has been made for several reasons:
1) CCP is a processor, and not a piece of open-ended software. 
2) Object orientated programming is easier for the code author, [but is pretty rubish at a lot of stuff](https://thenewstack.io/why-are-so-many-developers-hating-on-object-oriented-programming/)!
3) Widening accessibility. CryoSat scientists come from a variety of backgrounds and do not always know object orientated programming.

A final reason is that many people know OOP but far fewer know how or when to do it well!
