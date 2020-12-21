# -*- mode: python ; coding: utf-8 -*-

import sys
sys.setrecursionlimit(5000)
block_cipher = None
a = Analysis(['main.py'],
             pathex=['C:\\Users\\tmax\\PycharmProjects\\TextTransTool'],
             binaries=[],
             datas=[('textblob/en/*.txt', 'textblob/en'),('textblob/en/*.xml', 'textblob/en')],
             hiddenimports=['pkg_resources.py2_warn','pkg_resources.markers','nltk'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='TxtTransTool',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False)
