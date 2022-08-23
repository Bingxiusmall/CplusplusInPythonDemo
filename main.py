import ctypes
import io
import math
import sys
import re
import functools


class ostream:
    __intance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__intance:
            cls.__intance = super().__new__(cls)
        return cls.__intance

    def __lshift__(self, other):
        print(other, end=' \b')
        return self


class istream:
    __intance = None
    global __inputs

    def __new__(cls, *args, **kwargs):
        global __inputs
        __inputs = []
        if not cls.__intance:
            cls.__intance = super().__new__(cls)
        return cls.__intance

    def __init__(self, __inputs):
        self.id_inputs = id(__inputs)

    def __rshift__(self, other):
        try:
            if type(other) == type("string") or type(other) == type(123):
                global __inputs
                while 1:
                    if len(__inputs) > 0:
                        if __inputs[0] != '\n':
                            break
                    else:
                        break
                    __inputs.pop(0)
                if len(__inputs) == 0:
                    if stdinput != None:
                        __input = input()
                    for i in re.split(' ', __input):
                        __inputs.append(i)
                    __inputs.append('\n')
                __input = __inputs[0]
                __inputs.pop(0)
            if type(other) == type("string"):
                __id = id(other)
                __value = ctypes.cast(__id, ctypes.py_object).value
                bufsize = len(__value) + 1
                offset = sys.getsizeof(__value) - bufsize
                __new_size = sys.getsizeof(__input)
                start = __id + 24
                buf = ctypes.string_at(id(__input), __new_size)
                __sum = -1
                for i in __input:
                    __sum += 1
                    try:
                        ctypes.memset(__id + offset + __sum, ord(i), 1)
                    except Exception as e:
                        raise (RuntimeError(e))
                for addr, value in zip(range(start - 8, start), buf[16:24]):
                    ctypes.memset(addr, value, 1)
            elif type(other) == type(123):
                __input = int(__input)
                __id = id(other)
                __value = ctypes.cast(__id, ctypes.py_object).value
                __old_size = sys.getsizeof(__value)
                __new_size = sys.getsizeof(__input)
                start = __id + 24
                buf = ctypes.string_at(id(__input), __new_size)
                for pos, value in enumerate(buf[24:], start=start):
                    ctypes.memset(pos, value, 1)
                for addr, value in zip(range(start - 8, start), buf[16:24]):
                    ctypes.memset(addr, value, 1)
            else:
                __type = str(type(other))[8:-2]
                raise (InputError(
                    "\'" + __type + "\' object cannot be used in function \'cin\', you can try \'int\' object or \'str\' object"))
        except Exception as e:
            raise (RuntimeError(e))
        self.id_inputs = id(__inputs)
        return self

    def getline(self, other, letters, ending=None):
        global __inputs
        if type(other) == type("string"):
            if len(__inputs) == 0:
                if stdinput == None:
                    __input = input()
                for i in re.split(' ', __input):
                    __inputs.append(i)
                __inputs.append('\n')
            __input = ""
            while __inputs[0] != '\n':
                __input += __inputs[0]
                if ending != None:
                    including_id = __input.find(ending)
                    if including_id != -1:
                        __inputs[0] = __input[including_id:]
                        __input = __input[:including_id - 1]
                        if __inputs[0] == '':
                            __inputs.pop(0)
                        break
                if len(__input) > letters:
                    __inputs[0] = __input[letters:]
                    __input = __input[:letters]
                    break
                if __inputs[1] != '\n':
                    __input += ' '
                __inputs.pop(0)
            __inputs.pop(0)
            __id = id(other)
            __value = ctypes.cast(__id, ctypes.py_object).value
            bufsize = len(__value) + 1
            offset = sys.getsizeof(__value) - bufsize
            __new_size = sys.getsizeof(__input)
            start = __id + 24
            buf = ctypes.string_at(id(__input), __new_size)
            __sum = -1
            for i in __input:
                __sum += 1
                try:
                    ctypes.memset(__id + offset + __sum, ord(i), 1)
                except Exception as e:
                    raise (RuntimeError(e))
            for addr, value in zip(range(start - 8, start), buf[16:24]):
                ctypes.memset(addr, value, 1)
        else:
            __type = str(type(other))[8:-2]
            raise (InputError(
                "\'" + __type + "\' object cannot be used in function \'cin\', you can try \'str\' object"))
        self.id_inputs = id(__inputs)
        return self

    def reinput(self, inputid):
        self.id_inputs = inputid
        __inputs = ctypes.cast(cin.id_inputs, ctypes.py_object).value
        return self


class multidef:
    def less(a, b):
        return a < b

    def __init__(self):
        self.__type = None

    def __lt__(self, args):
        self.__type = args[0]
        try:
            self.__pred = args[1]
        except:
            self.__pred = less
        return self

    def __gt__(self, other=None):
        return multiset_bottle(self.__type, self.__pred)


class multiset_bottle:
    def __init__(self, multi_type: type, pred):
        self.__i = None
        self.__multiset = set()
        self.__multiset_count = dict()
        self.__type = multi_type
        self.__pred = pred

    def __str__(self):
        return str(+self)

    def __pos__(self):
        self.__multilist = list()
        for self.__i in self.__sort__():
            self.__multilist += self.__multiset_count[self.__i]*[self.__i]
        return self.__multilist

    def insert(self, elem):
        if type(elem) == self.__type:
            if elem in self.__multiset:
                self.__multiset_count[elem] += 1
            else:
                self.__multiset.add(elem)
                self.__multiset_count[elem] = 1
        else:
            raise(MultisetInsertingError("The {} multiset object cannot insert {} object".format(self.__type, type(elem))))

    def __sort__(self):
        self.__multiset_list = list(self.__multiset)
        return sorted(self.__multiset_list, key=functools.cmp_to_key(self.__pred))


class MultisetInsertingError(Exception):
    pass


class stdio:
    def __init__(self, stream):
        self.stream = stream


class FileError(Exception):
    pass


class InputError(Exception):
    pass


def less(a, b):
    return a < b

def greater(a, b):
    return a > b


def getline(self, other, ending=None):
    global __inputs, stderror
    __value = ctypes.cast(cin.id_inputs, ctypes.py_object).value
    if type(other) == type("string"):
        if len(__inputs) == 0:
            if stdinput == None:
                __input = input()
            for i in re.split(' ', __input):
                __inputs.append(i)
            __inputs.append('\n')
        __input = ""
        while __inputs[0] != '\n':
            __input += __inputs[0]
            if ending != None:
                including_id = __input.find(ending)
                if including_id != -1:
                    __inputs[0] = __input[including_id:]
                    __input = __input[:including_id]
                    if __inputs[0] == '':
                        __inputs.pop(0)
                    break
            if __inputs[1] != '\n':
                __input += ' '
            __inputs.pop(0)
        __inputs.pop(0)
        __id = id(other)
        __value = ctypes.cast(__id, ctypes.py_object).value
        bufsize = len(__value) + 1
        offset = sys.getsizeof(__value) - bufsize
        __new_size = sys.getsizeof(__input)
        start = __id + 24
        buf = ctypes.string_at(id(__input), __new_size)
        __sum = -1
        for i in __input:
            __sum += 1
            try:
                ctypes.memset(__id + offset + __sum, ord(i), 1)
            except Exception as e:
                raise (RuntimeError(e))
        for addr, value in zip(range(start - 8, start), buf[16:24]):
            ctypes.memset(addr, value, 1)
    else:
        __type = str(type(other))[8:-2]
        raise (InputError(
            "\'" + __type + "\' object cannot be used in function \'getline\', you can try \'str\' object"))
    cin.reinput(id(__inputs))


def freopen(path, mode, stream=None):
    global stdinput, stdoutput, stderror, __inputs
    if stream != None:
        fmode = stream
    else:
        if mode == "r":
            fmode = stdin;
        else:
            fmode = stdout;
    if fmode == stdin:
        stdinput = path
        with io.open(stdinput, "r") as file:
            finput = file.read()
        finput_list = re.split(r'\n', finput)
        while len(finput_list) > 0:
            __inputs.append(finput_list[0])
            finput_list.pop(0)
            if len(finput_list) > 0:
                __inputs.append('\n')
        cin.reinput(__inputs)
    elif fmode == stdout:
        stdoutput = path
        with io.open(stdoutput, "w") as file:
            file.truncate()
            sys.stdout = file
    elif fmode == stderr:
        stderror = path
        with io.open(stderror, "w") as file:
            file.truncate()
            sys.stderr = file
    else:
        raise (FileError("fmode must be stdin, stdout or stderr, but not " + str(mode)))


def fclose(stream):
    global stdinput, stdoutput, stderror, python_stdout, python_stderr
    if stream == stdin:
        stdinput = None
    elif stream == stdout:
        stdoutput = None
        sys.stdout = python_stdout
    elif stream == stderr:
        stderror = None
        sys.stderr = python_stderr
    else:
        if type(stream) == type(stdin):
            raise (FileError("stream must be stdin, stdout or stderr, but not stdio." + str(stream.stream)))
        else:
            raise (FileError("stream must be stdin, stdout or stderr, but not " + str(type(stream))[1:-1]))


def __gcd(x, y):
    return math.gcd(x, y)


def log(x):
    return math.log(x)


def log2(x):
    return math.log2(x)


def log10(x):
    return math.log10(x)


def log1p(x):
    return math.log1p(x)


def exp(x):
    return math.exp(x)


def perm(x, k=None):
    return math.perm(x, k)


__inputs = []
cout = ostream()
cin = istream(__inputs)
stdin = stdio("stdin")
stdout = stdio("stdout")
stderr = stdio("stderr")
multiset = multidef()
python_stdout = sys.stdout
python_stderr = sys.stderr
stdinput = None
stdoutput = None
stderror = None
endl = '\n'


# Here to program :)
# How to use?
# > use "cin>>a>>b>>c>>......" to read just a word.
# > use "cout<<a<<b<<c<<'what'<<......" to write.
# > use "cin.getline(d,25)" or "cin.getline(d,25,'#')" to read just 25 words and none-'#'.
# > use "getline(cin,e)" or "getline(cin,e,'#')" to read a line and none-'#'.
# > use "freopen(path,mode)" or "freopen(path,mode,stream)" to get file.[mode] must be stdin,stdout,stderr.
# > use "fclose(stream)" to end a file reading.
# > use "__gcd(x,y)","log(x)","log2(x)","log10(x)","log1p(x)","exp(x)","perm(x)" to do just themselves
# > multiset descriptions:
# > > because of some reasons of python, you need to write 'var_name = (multiset<(multi_type, cmp(optional, but the
# > > > comma in front of this must be there, or not python will be mistaken)))>None' to create a multiset object
# > > I had already do what I can, but I cannot do opposite python grammar :(
# > > use 'insert(elem)' to insert an element
# > > use 'var_name' to get a string of the multiset object
# > > use '+var_name(there is a plus in front of var_name)' to get a list of the multiset object
# > > just these, other I haven't do, wait to see XD
# There's some bugs,when you find a bug,you can ask in issues.
