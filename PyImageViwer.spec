# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.pyw'],
             pathex=['D:\\gergely\\Programming\\PyImageViewer'],
             binaries=[('C:\Python38\Lib\site-packages\shiboken2\shiboken2.abi3.dll', '.')],
             datas=[],
             hiddenimports=[],
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
          name='PyImageViewer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          icon="images/PyImageViewer.ico",
          console=True )
