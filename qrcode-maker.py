#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = [
#   "pillow>=10.4",
#   "qrcode-artistic>=3.0.2",
#   "segno>=1.6.6",
# ]
# ///

# ABOUTME: Generates branded QR codes with an embedded background image.
# Uses segno and qrcode-artistic to overlay a logo onto a QR code.

import segno

target_link = "https://bit.ly/pytexas2024"
background_image = "./logo.png"
output_file = "pytexas.png"

qrcode = segno.make(target_link, micro=False)
qrcode.to_artistic(background=background_image, target=output_file, scale=20)
