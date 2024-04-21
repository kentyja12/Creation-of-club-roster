import os
import sys
import datetime
import pandas as pd
from openpyxl import load_workbook
import tkinter
from tkinter import messagebox

from module.Gakuban_append_flow import gakuban_append_flow
from module.Write_xlsx import write_xlsx
from module.File_load import file_load
from module.Register_list import register_list
from module.Print_xlsx import print_xlsx
from module.Instant_meibo_register import instant_meibo_register
from module.Meibo_clear import meibo_clear

from Class import tmp
from Class import student_data
from Class import default

class Application(tkinter.Frame):

    def at_least_char(self,string): #文字列が入らない限りボタンを押せないようにする。
        if len(string)<=0:
            self.Button_print_xlsx['state'] = 'disabled'
            self.Button['state'] = 'disabled'
            self.Button2['state'] = 'disabled'
            self.Button4['state'] = 'disabled'            
        else:
            self.Button_print_xlsx['state'] = 'normal'
            self.Button['state'] = 'normal'
            self.Button2['state'] = 'normal' 
            self.Button4['state'] = 'normal'            
        return True

    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        master.title(u"出席確認")
        master.geometry("400x310")
        master.iconbitmap(default=os.path.join(os.path.dirname(__file__),"resources\mainIcon.ico")) #icon画像の設定
        self.msg = tkinter.StringVar()

        vc1 = self.register(self.at_least_char)
        #Label：クラブ名入力欄メッセージ
        Static0 = tkinter.Label(text=u'団体名：')
        Static0.place(x=60,y=275)

        #Entry：クラブ名入力ボックス
        self.EditBox_print_xlsx = tkinter.Entry(width=20,
                                                validatecommand=(vc1,"%P"),
                                                validate='all')
        self.EditBox_print_xlsx.place(x=120,y=275)

        #Button：名簿出力ボタン
        self.Button_print_xlsx = tkinter.Button(text=u'名簿出力',
                                                state='disabled',
                                                command=self.get_from_EditBox_print_xlsx_to_class)
        self.Button_print_xlsx.place(x=250,y=275)

        #Label：学籍番号入力欄メッセージ
        Static1 = tkinter.Label(text=u'学籍番号：')
        Static1.place(x=50,y=10)

        #Entry:学籍番号入力欄入力ボックス
        self.EditBox = tkinter.Entry(width=20)
        self.EditBox.bind('<Return>',self.get_from_EditBox_to_class)
        self.EditBox.place(x=120,y=10)

        #Button：学籍番号登録ボタン
        self.Button = tkinter.Button(text=u'出席登録', state="disabled")
        self.Button.bind("<Button-1>",self.get_from_EditBox_to_class)
        self.Button.place(x=250,y=10)

        #Label：メッセージ表示見出し部分
        Static4 = tkinter.Label(text=u'【状態】')
        Static4.place(x=10,y=50)

        #Frame：ボタン群のフレーム
        actionButton_frame = tkinter.LabelFrame(self)
        actionButton_frame.grid(column=0,row=0)

        #Button：名簿読み込み
        Button0 = tkinter.Button(text=u'名簿読み込み')
        Button0.bind("<Button-1>",file_load)
        Button0.place(x=20,y=130)

        #Button：登録リスト
        self.Button4 = tkinter.Button(text=u'登録リスト', state="disabled")
        self.Button4.bind("<Button-1>",register_list)
        self.Button4.place(x=20,y=100)

        #Button：リストクリア
        self.Button3 = tkinter.Button(text=u'リストクリア',
                                    state='disabled',
                                    command=self.give_to_meibo_clear)
        self.Button3.place(x=85,y=100)

        #Label：学籍番号
        self.Static_instant1 = tkinter.Label(text=u'学籍番号')
        self.Static_instant1.place(x=250,y=100)
        #Entry：学籍番号入力欄
        self.EditBox_instant1 = tkinter.Entry(width=20)
        self.EditBox_instant1.place(x=250,y=120)

        #Label：名前
        self.Static_instant2 = tkinter.Label(text=u'名前')
        self.Static_instant2.place(x=250,y=140)
        #Entry：名前入力欄 
        self.EditBox_instant2 = tkinter.Entry(width=20)
        self.EditBox_instant2.place(x=250,y=160)

        #Label：電話番号
        self.Static_instant3 = tkinter.Label(text=u'電話番号')
        self.Static_instant3.place(x=250,y=180)
        #Entry：電話番号入力欄
        self.EditBox_instant3 = tkinter.Entry(width=20)
        self.EditBox_instant3.place(x=250,y=200)

        #Button：インスタント名簿登録
        self.Button2 = tkinter.Button(text=u'インスタント名簿登録', state='disabled')
        self.Button2.bind("<Button-1>",self.get_from_EditBox_to_class_instant)
        self.Button2.place(x=250,y=230)

    def get_from_EditBox_to_class(self,EditBox):
        tmp.EditBox_tmp=self.EditBox.get()
        gakuban_append_flow(self)

    def get_from_EditBox_to_class_instant(self,EditBox):
        tmp.EditBox_instant1_tmp = self.EditBox_instant1.get()
        tmp.EditBox_instant2_tmp = self.EditBox_instant2.get()
        tmp.EditBox_instant3_tmp = self.EditBox_instant3.get()
        return instant_meibo_register(self)

    def get_from_EditBox_print_xlsx_to_class(self):
        student_data.club_name = self.EditBox_print_xlsx.get()
        return print_xlsx(self)

    def give_to_meibo_clear(self):
        return meibo_clear(self)

def main():
    root = tkinter.Tk()
    app = Application(master=root)
    root.mainloop()

if __name__ == '__main__':
    main()