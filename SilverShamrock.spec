# -*- mode: python -*-

block_cipher = None


a = Analysis(['SilverShamrock.py'],
             pathex=['C:\\devel\\SilverShamrock'],
             binaries=None,
             datas=[('pumpkin.ico', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='SilverShamrock',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='pumpkin.ico')
