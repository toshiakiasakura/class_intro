import re 
from typing import Union, Optional, List, Dict, Callable, Any
from types import ModuleType
import functools


class FrameWork():
    def __init__(self):
        print(f"# {self.name}:")
        self.greet_dic = {
            "English": "Hello",
            "Japanese": "こんにちは",
            "German": "Hallo",
        }

        self.greet_list = list(self.greet_dic.values())

        self.check_greet_dic = {
            "English": "Hello",
            "Japanese": "こんにちは",
            "German": "Hallo",
            "Spanish": "Hola",
            "Russian": "Здравствуйте",
            "Chinese": "你好啊",
        }
        self.check_greet_list = list(self.check_greet_dic.values())

    def print_explanation(self):
        print("## Explanation:")
        print(self.explanation)

    def print_answer(self, hide_answer=False):
        print(f"< Exmaple Input type > \n{type(self.input)}\n")
        print(f"< Exmaple Input > \n{self.input}\n")
        if not hide_answer:
            print(f"< Example Answer type > \n{type(self.ans)}\n")
            print(f"< Example Answer output with print> \n{self.ans}\n")
            print(f"< Example Answer output with repr> \n{repr(self.ans)}")

    def check_two_variables_are_same(self, v1, v2):
        if not type(v1) == type(v2):
            print("WWWWWWWWWWWWWWWWWWWW Answer type is not correct WWWWWWWWWWWWWWWWWW")
            return (False)
        else:
            if v1 == v2:
                return(True)
            else:
                print("WWWWWWWWWWWWWWWWWWWWWWW Not Correct WWWWWWWWWWWWWWW")

def error_wrapper(func):
    @functools.wraps(func)
    def inner(*args, **kargs):
        try:
            func(*args, **kargs)
        except Exception as e:
            print("WWWWWWWWWWWWWWWWWW Function or method can not run correctly WWWWWWWWWWWW")
            print(e)
    return(inner)

class q1(FrameWork):
    name = "Question1"

    def __init__(self): 
        super().__init__()
        self.explanation = """I want to become multilingual person. 
First, I want to master the various greetings.  \n
Given the string, write the function to say "<greet word> world! うーにゃー" string.
Next, write the same functionality using class. 
"""

        self.print_explanation()
        self.input = "こんにちは"
        self.ans = self.__generate__answer(self.input)
        self.print_answer()
    
    def __generate__answer(self, hello):
        ans = f"{hello} world! うーにゃー"
        return(ans)

    @error_wrapper
    def check_answer(self, ans_f: Callable[[str], str]):
        flags = []
        for word in self.check_greet_list:
            print("input is : ",word)
            sub_ans = ans_f(word)
            ans = self.__generate__answer(word)
            flag = self.check_two_variables_are_same(sub_ans, ans)
            flags.append(flag)
        if all(flags):
            print("!!!! Correct! congraturations!!!!!!")

class q2(FrameWork):
    name = "Question2"

    def __init__(self):
        super().__init__()
        self.explanation = """I do not satisfy with this result. 
Everyone can repeat the word if given. 
So I want to say the word given the language.  \n
Write the class to say "<greet word> world! うーにゃー" string given 
the language name. 
The dictionary of languages and words are given. 
The method should only accept one language name.
"""

        self.print_explanation()
        self.input = "Japanese"
        self.item = self.greet_dic
        self.ans = self.__generate__answer(self.input)
        self.print_answer()

    def __generate__answer(self, lang):
        word = self.check_greet_dic[lang]
        ans = f"{word} world! うーにゃー"
        return(ans)

    @error_wrapper
    def check_answer(self, ans_f: Callable[[str],str]):
        flags = []
        for v in self.greet_dic.keys():
            sub_ans = ans_f(v)
            ans = self.__generate__answer(v)
            flag = self.check_two_variables_are_same(sub_ans, ans)
            flags.append(flag)
        if all(flags):
            print("!!! Well done !!!!")

class q3(FrameWork):
    name = "Question3"

    def __init__(self): 
        super().__init__()
        self.explanation = """Got it. Like mulitilinguer I am!!!.
But... I can only say with "<greeting word> world! うーにゃー"????? 
I also want to say "<greeting word> うーにゃー!", "<greeting word> うーにゃーうーにゃー!". 
Can you write those functions named "say1", "say2", "say3"? 

Each function recieves the language name, and should return 
"<greeting word> world! うーにゃー" for say1 
"<greeting word> うーにゃー!" for say2
"<greeting word> うーにゃーうーにゃー!" for say3.

The dictionary of languages and words are given in item part.
Pass the class with those methods to the answer. 
"""
        self.print_explanation()
        self.input = "Japanse"
        self.item = self.greet_dic
        class Ans():
            item = self.item
            def say1(self, lang):
                word = self.item[lang]
                return(f"{word} world! うーにゃー")

            def say2(self, lang):
                word = self.item[lang]
                return(f"{word} うーにゃー!")

            def say3(self, lang):
                word = self.item[lang]
                return(f"{word} うーにゃー!")
        self.ans = Ans
        self.print_answer(hide_answer=True)
    
    @error_wrapper
    def check_anwer(self, ans_cls: object):
        flags = []
        obj_ans = self.ans()
        obj_sub = ans_cls()
        for v in self.greet_dic.keys():
            for i in range(1,4):
                m_name = f"say{i}"
                m_ans = getattr(obj_ans, m_name)
                m_sub = getattr(obj_sub, m_name)
                flag = self.check_two_variables_are_same(m_ans(v), m_sub(v))
                flags.append(flag)
        if all(flags):
            print(" Got Got Got it. I can say various sentences. Thank you!!!!")
            print(" YAAHHOHOHAOHOAHOHAOHOAHOHAOHOAHOHAOH")

class q4(FrameWork):
    name = "Question4"

    def __init__(self):
        super().__init__()
    
        self.explanation = """My vocablary expanding!!!!!!!! 
Thank you! Thank you! I'm very glad!!!!!!!!!!!!!!!!! うーにゃー!

...
...
...

WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
Yesterday, I tried to sleep... I counted a lot of　
"(」・ω・)」うー！(/・ω・)/にゃー！"
However, one time, I made mistake, and said 
"(「・ω・)「うー！(\・ω・)\にゃー！"

I am very sad, too sad... 
I want to fix this word. 

Oh, You should help me fix the word.
T counted 10000 times of うーにゃー. 

Those are stored in say{n} method of this instance. 
Please find the one method which return 
"(「・ω・)「うー！(\・ω・)\にゃー！"

and fix this method to return 
"(」・ω・)」うー！(/・ω・)/にゃー！"

Pass the fixed instance as the answer. 
"""
        self.print_explanation()

        def f():
            return( "(」・ω・)」うー！(/・ω・)/にゃー！" ) 
        def g():
            return( "(「・ω・)「うー！(\・ω・)\にゃー！")
        def bonus():
            return( "You correctly run the for loop. Raise your hands!!!")

        for i in range(1,10001):
            setattr(self, f"say{i}", f)

        setattr(self, "say7026", g)
        setattr(self, "say10000", bonus)

    @error_wrapper
    def check_answer(self):
        if self.say7026() =="(」・ω・)」うー！(/・ω・)/にゃー！": 
            print("うーにゃー　正解だにゃー") 
        else:
            s = ""
            for i in range(10000):
                s += "(」・ω・)」うー！(/・ω・)/にゃー！" 
            print(s)

class q5(FrameWork):
    name = "Question5"

    def __init__(self):
        super().__init__()
        
        self.explanation = """ 
(「・ω・)「うー！(\・ω・)\にゃー！
(」・ω・)」うー！(/・ω・)/にゃー！
(「・ω・)「うー！(\・ω・)\にゃー！
(」・ω・)」うー！(/・ω・)/にゃー！

Oh, I can't escape from these words. 

(「・ω・)「うー！(\・ω・)\にゃー！
(」・ω・)」うー！(/・ω・)/にゃー！
(「・ω・)「うー！(\・ω・)\にゃー！
(」・ω・)」うー！(/・ω・)/にゃー！

So, when I calculate plus, 
I can answer at one time. 
However, I can't answer the next plus calculation...

Edit the Vector class and write a code to achive the below result.

>>> a = Vector(1,2)
>>> b = Vector(3,4)
>>> c = a + b 
>>> print(c) 
(4,6) 
>>> repr(c)
'(4, 6)'
>>> d = c + a
>>> print(d) 
(「・ω・)「うー！(\・ω・)\にゃー！
(」・ω・)」うー！(/・ω・)/にゃー！
(「・ω・)「うー！(\・ω・)\にゃー！
(」・ω・)」うー！(/・ω・)/にゃー！
>>> repr(d)
'(「・ω・)「うー！(\\・ω・)\\にゃー！\n(」・ω・)」うー！(/・ω・)/にゃー！\n(「・ω・)「うー！(\\・ω・)\\にゃー！'

"""
        self.print_explanation()

    @error_wrapper
    def check_answer(self, ans_cls: object):
        a = ans_cls(1,2)
        b = ans_cls(3,4)
        c = a + b
        d = c + a 
        flag1 = False
        flag2 = False
        if c.__repr__() == '(4, 6)':
            flag1 = True
        if d.__repr__() == '(「・ω・)「うー！(\\・ω・)\\にゃー！\n(」・ω・)」うー！(/・ω・)/にゃー！\n(「・ω・)「うー！(\\・ω・)\\にゃー！':
            flag2 = True
        if flag1 and flag2:
            print("GREAT!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("GREAT!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("WELL DONE!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            print("Please try agein.")

class Vector():
    """Answer for the question 5.
    """
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        self.string = x 
        self.flag1 = False
        self.flag2 = False
        
    def __repr__(self):
        if self.flag1 and self.flag2:
            return(self.string)
        else:
            return(f"({self.x}, {self.y})")
    
    def __add__(self, cls):
        x = self.x + cls.x
        y = self.y + cls.y
        new_inst = self.__class__(x,y)
        new_inst.string = """(「・ω・)「うー！(\・ω・)\にゃー！
(」・ω・)」うー！(/・ω・)/にゃー！
(「・ω・)「うー！(\・ω・)\にゃー！"""
        if self.flag1:
            new_inst.flag1 = True
            new_inst.flag2 = True
        if not self.flag1:
            new_inst.flag1 = True
        
        return(new_inst)
    




class questions(FrameWork):
    title = "This class contains the following questions." 

    def __init__(self): 
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5 

        print(self.title)
        for d in dir(self):
            if re.findall("q\d+", d):
                print("- ", getattr(self, d).name)
                



