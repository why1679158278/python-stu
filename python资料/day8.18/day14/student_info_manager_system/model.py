class StudentModel:
    """
        学生模型
            用于封装V与C传递的数据
    """

    def __init__(self, name="", sex="", score=0.0, age=0, sid=0):
        self.name = name
        self.sex = sex
        self.score = score
        self.age = age
        self.sid = sid

    def __str__(self):
        return f"{self.name}的编号是{self.sid},年龄是{self.age},性别是{self.sex},成绩是{self.score}"

    def __eq__(self, other):
        return self.sid == other.sid