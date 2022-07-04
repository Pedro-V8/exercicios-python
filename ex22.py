from logging import raiseExceptions


class Container:
    """
    A container of integers that should support
    addition, removal, and search for the median integer
    """
    def __init__(self):
        self.my_list = []
        pass

    def add(self, value: int) -> None:
        self.my_list.append(value)
        print(self.my_list)
        
        
        """
        Adds the specified value to the container

        :param value: int
        """
        # TODO: implement this method
        pass

    def delete(self, value: int) -> bool:
        #print(self.my_list)
        if value in self.my_list:
            index = self.my_list.index(value)
            self.my_list.pop(index)
            return True
        else:
            print("NAO")
            return False
            
            
        """
        Attempts to delete one item of the specified value from the container

        :param value: int
        :return: True, if the value has been deleted, or
                 False, otherwise.
        """
        # TODO: implement this method
        return False

    
    def get_median(self) -> int:
        """
        Finds the container's median integer value, which is
        the middle integer when the all integers are sorted in order.
        If the sorted array has an even length,
        the leftmost integer between the two middle 
        integers should be considered as the median.

        :return: The median if the array is not empty, or
        :raise:  a runtime exception, otherwise.
        """
        try:
            if len(self.my_list) == 0:
                raiseExceptions
            result = sum(self.my_list)
            print(result)

        except IndexError as err:
            print("IndexError: {}".format(err))
        # TODO: implement this method
        return 0



obj = Container()

obj.get_median()