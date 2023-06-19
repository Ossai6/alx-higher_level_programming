class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        if attrs is None:
            return {'first_name': self.first_name, 'last_name': self.last_name, 'age': self.age}
        else:
            result = {}
            for attr in attrs:
                if attr == 'first_name' and hasattr(self, 'first_name'):
                    result[attr] = self.first_name
                elif attr == 'last_name' and hasattr(self, 'last_name'):
                    result[attr] = self.last_name
                elif attr == 'age' and hasattr(self, 'age'):
                    result[attr] = self.age
            return result

