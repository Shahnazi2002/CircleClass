class Circle:
    '''
    Calculate the circumference(c) and area(a) of a circle.

    Attributes:
        r (float): The size of the radius.
        pi (float, optional): The desired value for the pi number.
    '''

    def __init__(self, r: float, pi: float = 3.14):
        '''
        The constructor for Circle class.

        Parameters:
            r (float): The size of the radius.
            pi (float, optional): The desired value for the pi number.
        '''
        self.r = r
        self.pi = pi

    def c(self) -> float:
        '''
        The function to calculate the circumference.
        '''
        return 2*self.pi*self.r

    def a(self) -> float:
        '''
        The function to calculate the area.
        '''
        return self.pi*self.r*self.r