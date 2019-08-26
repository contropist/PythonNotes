def handle(conf):
# 重要: 请务必把任务(jobs)中需要保存的文件存放在 results 文件夹内
# Important : Please make sure your files are saved to the 'results' folder in your jobs
    2 + 2
    2.0 + 2.5
    2 + 2.5
    a = 0.2
    s = "hello world"
    s
    s = 'hello world'
    s
    s = """hello
    world"""
    print (s)
    s = '''hello
    world'''
    print (s)
    s = "hello" + " world"
    s
    s[0]
    s[-1]
    s[0:5]
    s = "hello world"
    s.split()
    len(s)
    a = [1, 2.0, 'hello', 5 + 1.0]
    a
    a + a
    a[1]
    len(a)
    a.append("world")
    a
    s = {2, 3, 4, 2}
    s
    len(s)
    s.add(1)
    s
    a = {1, 2, 3, 4}
    b = {2, 3, 4, 5}
    a & b
    a | b 
    a - b
    a ^ b
    d = {'dogs':5, 'cats':4}
    d
    len(d)
    d["dogs"]
    d["dogs"] = 2
    d
    d["pigs"] = 7
    d
    d.keys()
    d.values()
    d.items()
    from numpy import array
    a = array([1, 2, 3, 4])
    a
    a + 2
    a + a
    %matplotlib inline
    from matplotlib.pyplot import plot
    plot(a, a**2)
    line = '1 2 3 4 5'
    fields = line.split()
    fields
    total = 0
    for field in fields:
        total += int(field)
    total
    numbers = [int(field) for field in fields]
    numbers
    sum(numbers)
    sum([int(field) for field in line.split()])
    cd ./
    f = open('data.txt', 'w')
    f.write('1 2 3 4\n')
    f.write('2 3 4 5\n')
    f.close()
    f = open('data.txt')
    data = []
    for line in f:
        data.append([int(field) for field in line.split()])
    f.close()
    data
    for row in data:
        print (row)
import os
    os.remove('data.txt')
    def poly(x, a, b, c):
        y = a * x ** 2 + b * x + c
        return y

    x = 1
    poly(x, 1, 2, 3)
    x = array([1, 2, 3])
    poly(x, 1, 2, 3)
    from numpy import arange

    def poly(x, a = 1, b = 2, c = 3):
        y = a*x**2 + b*x + c
        return y

    x = arange(10)
    x
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    poly(x)
    poly(x, b = 1)
import os
    os.getpid()
    os.sep
    class Person(object):
        def __init__(self, first, last, age):
            self.first = first
            self.last = last
            self.age = age
        def full_name(self):
            return self.first + ' ' + self.last
    person = Person('Mertle', 'Sedgewick', 52)
    person.first
    person.full_name()
    person.last = 'Smith'
    person.critters = d
    person.critters
    url = 'http://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv'
    import urllib.request

    aa = urllib.request.urlopen(url)
    ge_csv = aa.read()
    data = []
    for line in ge_csv:
        data.append(line)
    data[:4]
    pass
    # return your result consistent with .yml you defined
    # .e.g return {'iris_class': 1, 'possibility': '88%'}


if __name__ == '__main__':
    conf = {}
    handle(conf)
