#build.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

paths=['./meibo/',
        './meibo/module',
        './meibo/module/sub_module',
        './meibo/resources'
]

added_files=[
    ("meibo/resources", "resources"),  # アイコンファイルも絶対パスで指定
    ("meibo/module", "module"),
    ("meibo/module/sub_module", 'module/sub_module')
]

hidden_imports=[
"tkinter",
"tkinter.messagebox",
"module.Gakuban_append_flow",
"module.Write_xlsx",
"module.File_load",
"module.Register_list",
"module.Print_xlsx",
"module.Instant_meibo_register",
"module.Meibo_clear",
"module.sub_module.Make_df_from_list"
]

a = Analysis(['./meibo/__main__.py'],
             pathex=paths,
             binaries=[],
             datas=added_files,
             hiddenimports=hidden_imports,
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,  # 更新したbinariesリストを使う
          a.zipfiles,
          a.datas,
          [],
          name='meibo',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='meibo/resources/mainIcon.ico', 
          onefile=True)  # 単一ファイル生成のオプション

dist_path = 'dist'  # 出力ディレクトリのパス
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='meibo',
               path=dist_path)
