import tkinter
from tkinter import messagebox
from Class import tmp
from Class import student_data
from Class import default

def gakuban_append_flow(app): 
    '''
    学籍番号の重複チェック、定員数チェック、名簿上に載ってるかをチェック
    student_data.gakuban_listへの格納
    Check for duplicate student number, check for maximum number of students, and check if there is  the student on the list.
    Store to student_data.gakuban_list.
    '''
    #「状態」メッセージの表示座標
    X = 60
    Y = 50

    gakuban_tmp = tmp.EditBox_tmp.upper() # 学籍番号を取得し、文字を大文字に変更

    Static3 = tkinter.Label(text=u"") #「状態」のメッセージ欄の初期化
    Static3.place_forget() #「状態」のメッセージ欄の非表示

    # 複数の学番が同時に入力された際は、全部処理する
    for gakuban_tmp_value in gakuban_tmp.split():
        if type(student_data.df_meibo) == str: # 名簿が読み込まれているかチェック
            app.msg.set("名簿が読み込まれていません。名簿を読み込んでください。")
            Static3 = tkinter.Label(textvariable=app.msg)
            Static3.place(x=X,y=Y)
        elif student_data.count >= default.limit_count: # 学籍番号の数が集会名簿の上限を超えているかチェック
            app.msg.set("名簿に登録できる人数の上限に達しました。\n一度出力し、新規名簿を作成してください。")
            Static3 = tkinter.Label(textvariable=app.msg)
            Static3.place(x=X,y=Y)
            app.Button['state'] = 'disabled'
            app.Button2['state'] = 'disabled'
        elif not any(student_data.df_meibo["学籍番号"].isin([gakuban_tmp_value])): # 読み込んだ名簿上に学籍番号があるかチェック 
            app.msg.set("あなたの学籍番号は名簿上にありません。\n部外者の場合は、インスタント名簿登録を行ってください。")
            Static3 = tkinter.Label(textvariable=app.msg)
            Static3.place(x=X,y=Y)
        elif gakuban_tmp_value in student_data.gakuban_list: # 登録予定のリストに既にあるかチェック
            app.msg.set("{}は既に登録されています。".format(gakuban_tmp_value))
            Static3 = tkinter.Label(textvariable=app.msg)
            Static3.place(x=X,y=Y) 
        else: # リストに学籍番号の格納
            student_data.gakuban_list.append(gakuban_tmp_value)
            app.msg.set("{}の登録に成功しました。".format(gakuban_tmp_value))
            Static3 = tkinter.Label(textvariable=app.msg)
            Static3.place(x=X,y=Y) 
            student_data.count = student_data.count +1 
            if len(student_data.gakuban_list) == 1:
                app.Button3['state'] = 'normal' #名簿クリアボタンを有効
            app.EditBox.delete(0,tkinter.END)