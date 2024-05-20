# qrcode-maker
Code used to make our cool QR Codes. It uses the `segno` and `qrcode-artistic` 
libraries.

<img src="example-output.png" width="200">

## Usage

1. `pip` install the `segno` and `qrcode-artistic` libraries, either manually or 
using the provided requirements file
1. Update the `target_link` variable with the link you want the QR Code to point to
1. Update the `background_image` variable with the image you want to be embedded in
the QR Code
1. Update the `output_file` variable with what you want the QR Code to be named
1. Run the file with `python qrcode-maker.py`. The resulting QR Code should 
appear in the same directory as the source code.


## Notes
If your image has a transparent background you may get some distortion in the 
resulting QR Code. We were able to fix this by removing the background using an
online image background remover. 
