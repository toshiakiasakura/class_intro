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

    def print_answer(self):
        print(f"< Exmaple Input type > \n{type(self.input)}\n")
        print(f"< Exmaple Input > \n{self.input}\n")
        print(f"< Example Answer type > \n{type(self.ans)}\n")
        print(f"< Example Answer output with print> \n{self.ans}\n")
        print(f"< Example Answer output with repr> \n{repr(self.ans)}")

    def check_two_variables_are_same(self, v1, v2):
        if not type(v1) == type(v2):
            print("WWWWWWWWWWWWWWWWWWWW Answer type is not correct WWWWWWWWWWWWWWWWWW")
            return ()
        else:
            if v1 == v2:
                print("Correct answer!")
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
        for word in self.check_greet_list:
            print("input is : ",word)
            sub_ans = ans_f(word)
            ans = self.__generate__answer(word)
            self.check_two_variables_are_same(sub_ans, ans)

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

    def check_answer(self, ans_f: Callable[[str],str]):
        for v in self.greet_dic.keys():
            sub_ans = ans_f(v)
            ans = self.__generate__answer(v)
            self.check_two_variables_are_same(sub_ans, ans)


class questions(FrameWork):
    title = "This class contains the following questions." 

    def __init__(self): 
        self.q1 = q1
        self.q2 = q2

        print(self.title)
        for d in dir(self):
            if re.findall("q\d+", d):
                print("- ", getattr(self, d).name)
                



