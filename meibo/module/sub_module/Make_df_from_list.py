from Class import student_data

def make_df_from_list(gakuban_list): 
    '''
    gakuban_listを元にDFを作成
    Create DF based on gakuban_list.

    paramaters
        gakuban_list : list
            出力予定の学籍番号のリスト
    '''

    for gakuban in gakuban_list:
        student_data_value = student_data.df_meibo[student_data.df_meibo['学籍番号']==gakuban] # 読み込んだ名簿と照合して、学生番号が一致した行（学生情報）を取り出す。
        if gakuban not in list(student_data.df["学籍番号"]): #出力予定の名簿に今から追加する学籍番号がないかチャック
            student_data.df = student_data.df.append(student_data_value) #学生情報をデータフレームに追加する。
    student_data.df = student_data.df.reset_index(drop=True) #indexがバラバラなのを統一する。
