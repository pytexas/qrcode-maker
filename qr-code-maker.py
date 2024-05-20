import io
import segno

qrcode = segno.make('https://bit.ly/pytexas2024', micro=False)
qrcode.to_artistic(background='./logo.png', target='pytexas.png', scale=20)