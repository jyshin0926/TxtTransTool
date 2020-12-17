#-*- coding: utf-8 -*-

import tkinter

from tkinter import *
from functools import partial
from converter import *


def convert_into_textarea(textArea, input):
    converted_input = combtxt(input.get())
    textArea.insert(1.0, converted_input + '\n')
    textField.delete(0, 'end')


# 화면 그리기
root = Tk()
root.title("이중전사 변환기")
root.geometry("390x770+100+100")


root.resizable(width=False, height=False)


# 결과값 변수 선언
result = StringVar()

# 텍스트 필드 그리기 및 변수 선언
textField = Entry(root, textvariable=result, width=30) # Entry는 자신이 만든 객체를 리턴함
textField.grid(row=1, column=1, columnspan=3, padx=25, pady=5) # grid는 상태 변화 함수임 쉽게 말해 return Type void와 같음

# show_result = partial(show_result, lb, result)

btn = Button(root, text="Enter(변환)", width=10, command=lambda: convert_into_textarea()) # 위와 동일
btn.grid(row=1, column=4, pady=10);

# 엔터 눌렀을 때 이벤트 거는 것
# root.bind('<Return>', lambda event: show_result())
root.bind('<Return>', lambda event: convert_into_textarea())

textArea = Text(root, width=49, height=50)
textArea.grid(row=2, column=1, columnspan=4, padx=15) 

convert_into_textarea = partial(convert_into_textarea, textArea, result)

label = Label(root, text = "Developer \n jyshin0926 (github) \n sjy777star@gmail.com ")
label.grid(row=3, column=1, columnspan=4, padx=25, pady=10)


root.mainloop()