class Class:
    count = 0
    @staticmethod
    def get_number():
        if Class.count > 1:
            Class.count *= 2
        else:
            Class.count += 1
        return Class.count
      