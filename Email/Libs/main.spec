# -*- mode: python -*-

block_cipher = None


a = Analysis(['..\\..\\..\\EmailSystem_\xcb\xd1\xcb\xf7_\xd7\xaa\xb7\xa2_\xbb\xd8\xb8\xb4_12.15\\Email\\Libs\\main.py'],
             pathex=['C:\\Users\\14356\\Desktop\\EMAILS~1.15\\Email\\Libs'],
             binaries=None,
             datas=None,
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
          exclude_binaries=True,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')
