"""
    A test utility module 

    lsdfjlksdjflksdjflksdjfklsdjflk
    sdlfjsdlkjsdklfjskldjfsdf
    sdfljsdkflsdjlksdjfkl

    Example
    -------
        >>> square(4)
        16

"""

def square(x):
    """
        Returns square of x
        
        How to use this function
        ------------------------
            >>> square(2)
            4

            >>> square("hello")
            Traceback (most recent call last):
            ...
            TypeError: argument must be a number

    """
    if type(x) not in (int, float, int, complex):
       raise TypeError("argument must be a number")

    return x*x


if __name__ == '__main__':
    import doctest
    doctest.testmod()








