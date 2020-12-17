import tkinter

from tkinter import *
from functools import partial


def output_result(textArea, result):
    output = result.get()
    print(result.get())
    textArea.insert(1.0, result.get() + '\n')
    textField.delete(0, 'end')

    return


# 화면 그리기
root = Tk()
root.title("이중전사 변환기")
root.geometry("390x780+100+100")



# 결과값 변수 선언
result = StringVar()

# 텍스트 필드 그리기 및 변수 선언
textField = Entry(root, textvariable=result, width=30) # Entry는 자신이 만든 객체를 리턴함
textField.grid(row=2, column=1, columnspan=3, padx=25, pady=10) # grid는 상태 변화 함수임 쉽게 말해 return Type void와 같음

# show_result = partial(show_result, lb, result)

btn = Button(root, text="Enter(변환)", width=10, command=lambda: output_result()) # 위와 동일
btn.grid(row=2, column=4, pady=10);

# 엔터 눌렀을 때 이벤트 거는 것
# root.bind('<Return>', lambda event: show_result())
root.bind('<Return>', lambda event: output_result())

textArea = Text(root, width=49, height=55)
textArea.grid(row=3, column=1, columnspan=4, padx=15) 

output_result = partial(output_result, textArea, result)

root.mainloop()