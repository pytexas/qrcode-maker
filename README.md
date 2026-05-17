# qrcode-maker
Code used to make our cool QR Codes. It uses the `segno` and `qrcode-artistic` 
libraries.

<img src="example-output.png" width="200">

## Usage

Requires [uv](https://docs.astral.sh/uv/).

1. Update the `target_link` variable with the link you want the QR Code to point to
1. Update the `background_image` variable with the image you want to be embedded in
the QR Code
1. Update the `output_file` variable with what you want the QR Code to be named
1. Run the file directly with `./qrcode-maker.py`. Thanks to [PEP 723](https://peps.python.org/pep-0723/) inline metadata and the script's `uv run` shebang, you don't need to manually create a venv. `uv` will create create one on script invocation, resolve the dependencies, and execute the code
1. The resulting QR Code appears in the same directory as the code


## Notes
If your image has a transparent background you may get some distortion in the 
resulting QR Code. We were able to fix this by removing the background using an
online image background remover. 
