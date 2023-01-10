from tkinter import messagebox
import pandas as pd

from Class import student_data
from Class import default

def meibo_clear(app):
    '''
    名簿リストをクリアする。
    Clear student_data.gakuban_list and student_data.df.
    '''
    if student_data.gakuban_list != [] or len(student_data.df['学籍番号']) != 0:
        surgeried_info = messagebox.askyesno("確認","名簿リストをクリアしますか？")
        if surgeried_info == True: 
            student_data.gakuban_list = [] #読み込んだ名簿から登録された学籍番号の初期化
            student_data.df = pd.DataFrame(columns=default.Columns) #インスタント名簿で登録された学生情報の初期化
            student_data.count = 0
            app.Button3['state'] = 'disabled' #ボタンの無効化
    
    return "break" #ボタンが押された状態を回避