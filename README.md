# CullRawByJPG

#### by Will Li | [https://github.com/williamli9300/CullRawByJPG/](https://github.com/williamli9300/CullRawByJPG/) | v0.1.0

A simple Python script to cull RAW files based on deleted JPEG files in a directory.
You can change the verbosity (i.e., is the name of every recycled file printed to console, or only the number of deleted files) by changing the value of `verbose` on line 11 to `True` or `False`.
Recommend `verbose = True` for < 700 files to delete, and `verbose = False` for > 700 files to delete, to prevent crashing.
You can change the number of files to give a status update if using `verbose = False` by changing `report_every_n_files` on line 12.

## How To Use (with JPEGs and your RAW format of choice)
1. Cull compressed photos by reviewing JPEGs and deleting (e.g. sending to Recycle Bin/Trash) undesired JPEGs.
2. Download the source code from [this link](https://github.com/williamli9300/CullRawByJPG/archive/refs/heads/main.zip) or from `<> Code` > `Download Zip` on the project front page, then extract the archive.
3. Copy the script `CullRawByJPG.py` into your desired directory containing RAW and JPEG files.
4. If your RAW format of choice is `*.CR3`, skip to Step 6. Otherwise, open `CullRawByJPG.py` in a text editor or IDE.
5. Change the `raw_type` variable on line 7 to your desired format, in uppercase, including the delimiter (`.`), according to the examples given.
6. Run the script by opening a Windows Command Prompt or macOS Terminal window in your desired directory, then running `python3 CullRawByJPG.py`.

## Using Other Compressed Formats
1. Open `CullRawByJPG.py` in a text editor or IDE.
2. Change the `compressed_type_1` and `compressed_type_2` variables on lines 8-9 to your desired format(s), in uppercase, including the delimiter (`.`), according to the examples given. If you are only using one compressed format, e.g. `.PNG`, keep `compressed_type_2 = ".JPEG"` (this part of the script shouldn't do anything if you don't have any JPEGs in your folder. If you *do* have JPEGs in your folder, change ".JPEG" to something that's not in any of the filenames, such as "LoremIpsumDolorSitAmet".)

## Compatibility, Dependencies, & Requirements
- Written in and requires Python 3.
- Requires the Python [Send2Trash library](https://pypi.org/project/Send2Trash/). Install using `python3 -m pip install Send2Trash` in Command Prompt or Terminal, or by following instructions given on the project page.
- Works with extensions that are both UPPERCASE or lowercase (e.g. `.CR3` and `.cr3`).
- Works with JPEGs using both `.JPG`/`.jpg` and `.JPEG`/`.jpeg` extensions.
- In theory, this script works on both Windows and macOS, but only tested on Windows 11.
- A folder containing RAW and JPEG files with the same names (minus extension). The script will search for RAW files without a correspondingly named JPEG file.
