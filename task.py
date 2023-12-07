""" Compare averages of two lists """

class ListAvgCompare:
    """ Compare averages of two lists class with first_list, second_list) fields"""
    def __init__(self, first_list, second_list):
        self.first_list = first_list
        self.second_list = second_list

    def compare_avg(self):
        """ Compare averages of two lists"""
        first_avg = self.find_avg(self.first_list)
        second_avg = self.find_avg(self.second_list)

        if first_avg > second_avg:
            message = 'Первый список имеет большее среднее значение'
        elif first_avg < second_avg:
            message = 'Второй список имеет большее среднее значение'
        else:
            message = 'Средние значения равны'
        return message

    def find_avg(self, numbers):
        """ Find average of list"""
        if not isinstance(numbers, list):
            raise TypeError("Input should be a list.")
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
