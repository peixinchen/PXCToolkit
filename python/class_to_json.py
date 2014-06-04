def to_json(python_object):
    '''自定义的json转换器'''
    #如果是对象，返回对象内部的__dict__字典
    if isinstance(python_object, object):
        return python_object.__dict__;
    #对内置类型，抛出异常，也就是使用json.dumps的默认处理方式
    raise TypeError(repr(python_object) + ' is not JSON serializable')
def toDict(obj):
    '''将任意对象转变了Python自带的dict类型'''
    import json;
    #调用dumps方法，将对象转变成为json格式的字符串
    #dumps的default参数指定了自定义的处理方法，这里将上面定义的to_json赋值给它。
    sTemp = str(json.dumps(obj,default=to_json));
    #将json格式的字符串转为dict对象
    return json.loads(sTemp);

#举例：  
class A1:
    def __init__(self):
        self.a = 0;
class B1:
    def __init__(self):
        self.b = 1;
        self.la = [A1(),A1()];
class C1(A1):
    def __init__(self):
        self.a = 2;
        self.c = [B1(),B1(),B1()];

if __name__ == '__main__':
    c1 = C1();    
    print toDict(c1);
  
    会输出：
    {u'a': 2, u'c': [{u'b': 1, u'la': [{u'a': 0}, {u'a': 0}]}, {u'b': 1, u'la': [{u'a': 0}, {u'a': 0}]}, {u'b': 1, u'la': [{u'a': 0}, {u'a': 0}]}]}
