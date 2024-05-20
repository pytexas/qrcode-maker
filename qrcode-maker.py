import segno

target_link = "https://bit.ly/pytexas2024"
background_image = "./logo.png"
output_file = "pytexas.png"

qrcode = segno.make(target_link, micro=False)
qrcode.to_artistic(background=background_image, target=output_file, scale=20)
