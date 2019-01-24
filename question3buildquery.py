from datetime import datetime

class Build_Query(object):
    def __init__(self):
        self.query = "SELECT * FROM Table WHERE "

    def set_query(self, addition):
        self.query += addition

    def greater_than(self, feild, value):
        self.set_query(" AND " + feild + " > " + str(value))

    def less_than(self, feild, value):
        self.set_query(" AND " + feild + " < " + str(value))

    def equal_to(self, feild, value):
        self.set_query(" AND " + feild + " = " + str(value))

    def IN(self, feild, value):
        self.set_query(" AND " + feild + " IN " + "(" + ",".join(str(i) for i in value) + ")")

    def NOT_IN(self, feild, value):
        self.set_query(" AND " + feild + " NOT IN " + "(" + ",".join(str(i) for i in value) + ")")

    def return_query(self):
        return self.query.replace("WHERE  AND","WHERE") + ";"
    

class ID():
    def __init__(self, build_query):
        self.build_query = build_query
        self.feild = "id"

    def greater_than(self, value):
        self.build_query.greater_than(self.feild, value)

    def less_than(self, value):
        self.build_query.less_than(self.feild, value)

    def equal_to(self, value):
        self.build_query.equal_to(self.feild, value)

    def IN(self, value):
        self.build_query.IN(self.feild, value)

    def NOT_IN(self, value):
        self.build_query.NOT_IN(self.feild, value)


class URL():
    def __init__(self, build_query):
        self.build_query = build_query
        self.feild = "url"

    def equal_to(self, value):
        self.build_query.equal_to(self.feild, value)


class Date():
    def __init__(self, build_query):
        self.build_query = build_query
        self.feild = "date"

    def greater_than(self, value):
        self.build_query.greater_than(self.feild, value.strftime("%Y-%m-%d"))

    def less_than(self, value):
        self.build_query.less_than(self.feild, value.strftime("%Y-%m-%d"))

    def equal_to(self, value):
        self.build_query.equal_to(self.feild, value.strftime("%Y-%m-%d"))


class Rating():
    def __init__(self, build_query):
        self.build_query = build_query
        self.feild = "rating"

    def greater_than(self, value):
        self.build_query.greater_than(self.feild, value)

    def less_than(self, value):
        self.build_query.less_than(self.feild, value)

    def equal_to(self, value):
        self.build_query.equal_to(self.feild, value)


if __name__ == '__main__':
    bq = Build_Query()
    
    qid = ID(bq)
    qdate = Date(bq)
    qurl = URL(bq)
    qrate = Rating(bq)

    qid.greater_than(5)
    qid.IN([3,4,5,6])
    qurl.equal_to("www.google.com")
    qdate.less_than(datetime.now())
    qrate.equal_to(20)

    print(bq.return_query())
