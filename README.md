# iFCon
A tool for handling iFAction resource file (iFCon file)

[![Build and Release](https://github.com/eWloYW8/iFCon/actions/workflows/release.yml/badge.svg)](https://github.com/eWloYW8/iFCon/actions/workflows/release.yml)

## Usage

You can directly run iFCon.py or install this module with pip:

```bash
pip install iFCon
```

```
positional arguments:  
  file                  The iFCon file to extract or pack.  

options:  
  -h, --help            show this help message and exit  
  -x, --extract         Extract the contents of an iFCon file.  
  -p PACK, --pack PACK  Pack the contents of a folder into an iFConfile.  
  -o OUTPUT, --output OUTPUT  
                        The output file for extracting the iFCon file.  
```

## Example

To extract the contents of an iFCon file, run the following command:

```
iFCon <iFCon file> -x -o <output folder>
```

To pack the contents of a folder into an iFCon file, run the following command:

```
iFCon <iFCon file> -p <folder>
```

## Disclaimer

This tool is provided for educational and informational purposes only. The author is not responsible for any misuse or damage caused by this tool. Use it at your own risk.