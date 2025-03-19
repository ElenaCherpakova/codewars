class Class:
    count = 1
    @staticmethod
    def get_number():
        res = Class.count
        Class.count *= 2
        return res