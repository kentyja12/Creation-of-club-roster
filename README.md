<span style="font-family: 'Times New Roman', Times, serif;">

# Creation of club roster App

**This application is designed for people who can understand Japanese.   
If you need the English version, please fork it.**

A tool for confirming attendees and integrating them into a template
Created for use in group activities.

### Features

* Loading of roster
* Verification of roster with student ID numbers
* Display of attendee list
* Addition of individuals not in the roster to the attendee list (Instant roster registration)
* Output of attendance list in a specific format (.xlsx)

### Development Period

3 months (1.5 months of actual operation)

### Version

* python 3.6.8
* openpyxl 3.0.10
* pandas 1.1.5

### Execution Method

#### Method (Run with python)

1. `pip install -r requirements.txt --user`
2. `python -m meibo`

### How to Use

#### Register attendance using the loaded roster

1. Load the roster from the "名簿読み込み" button. (When testing, load "example_meibo.xlsx".)
2. Enter the student ID number in the "学籍番号：" input box. (Supports both uppercase and lowercase)
3. Press the "出席登録" button.
4. Enter the group name (club name) in the "団体名：" input box.
5. When the "名簿出力" button becomes active, press the button to output.

#### Register individuals not in the loaded roster as attendees

1. Enter the "学籍番号", "名前", and "電話番号" in the input boxes of the Instant Roster Registration section.
   Input format
   * 学籍番号： 12XX123
   * 名前： Last First
   * 電話番号： 123-4567-8901
2. Press the "インスタント名簿登録" button.
3. Enter the group name (club name) in the "団体名" input box.
4. When the "名簿出力" button becomes active, press the button to output.

### Sample

#### Top Screen

* After loading the roster, enter the student ID number or input the instant roster

![default_window](images/default_window.png)

#### Screen During Input

![entered_window](images/entered_window.png)

#### Registration List Screen

* Displayed as the sum of attendees registered from the roster and attendees registered instantly

![registrants_list_window](images/registrants_list_window.png)

#### Example of Roster to Load

* The roster to load is in Excel format
* The order of genres for each column is fixed

![example_list](images/example_list.png)

#### Example of Output Screen

* The output format is only in xlsx format

![example_output_sheet](images/example_output_sheet.png)
