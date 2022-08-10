import ctypes
import io
import sys
import re


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
                    if stdinput!=None:
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
                raise (RuntimeError(
                    "\'" + __type + "\' object cannot be used in function \'cin\', you can try \'int\' object or \'str\' object"))
        except Exception as e:
            raise (RuntimeError(e))
        self.id_inputs = id(__inputs)
        return self

    def getline(self, other, letters, ending=None):
        global __inputs
        if type(other) == type("string"):
            if len(__inputs) == 0:
                if stdinput==None:
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
            raise (RuntimeError(
                "\'" + __type + "\' object cannot be used in function \'cin\', you can try \'str\' object"))
        self.id_inputs = id(__inputs)
        return self

    def reinput(self, inputid):
        self.id_inputs = inputid
        __inputs = ctypes.cast(cin.id_inputs, ctypes.py_object).value
        return self


class stdio:
    def __init__(self, stream):
        self.stream=stream


def getline(self, other, ending=None):
    global __inputs, stderror
    __value = ctypes.cast(cin.id_inputs, ctypes.py_object).value
    if type(other) == type("string"):
        if len(__inputs) == 0:
            if stdinput==None:
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
        raise (RuntimeError(
            "\'" + __type + "\' object cannot be used in function \'getline\', you can try \'str\' object"))
    cin.reinput(id(__inputs))


def freopen(path, mode, stream=None):
    global stdinput, stdoutput, stderror, __inputs
    if stream!=None:
        fmode = stream
    else:
        if mode=="r":
            fmode = stdin;
        else:
            fmode = stdout;
    if fmode==stdin:
        stdinput = path
        with io.open(stdinput, "r") as file:
            finput = file.read()
        finput_list = re.split(r'\n', finput)
        while len(finput_list)>0:
            __inputs.append(finput_list[0])
            finput_list.pop(0)
            if len(finput_list)>0:
                __inputs.append('\n')
        cin.reinput(__inputs)
    elif fmode==stdout:
        stdoutput = path
        with io.open(stdoutput, "w") as file:
            file.truncate()
            sys.stdout = file
    elif fmode==stderr:
        stderror = path
        with io.open(stderror, "w") as file:
            file.truncate()
            sys.stderr = file
    else:
        raise(RuntimeError("fmode must be stdin, stdout or stderr, but not " + str(mode)))


def fclose(stream):
    global stdinput, stdoutput, stderror, python_stdout, python_stderr
    if stream==stdin:
        stdinput = None
    elif stream==stdout:
        stdoutput = None
        sys.stdout = python_stdout
    elif stream==stderr:
        stderror = None
        sys.stderr = python_stderr
    else:
        raise(RuntimeError("fmode must be stdin, stdout or stderr, but not " + str(mode)))


__inputs = []
cout = ostream()
cin = istream(__inputs)
stdin = stdio("stdin")
stdout = stdio("stdout")
stderr = stdio("stderr")
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
# There's some bugs,when you find a bug,you can ask in issues.
