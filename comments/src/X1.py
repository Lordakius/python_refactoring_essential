class X1:

    @staticmethod
    def sum_of_squares(start, end):
        sum = 0

        for i in range(start, end + 1):
            sum += X1.square_of(i)

        return sum

    @staticmethod
    def square_of(k):
        return k * k
