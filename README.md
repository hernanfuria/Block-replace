# NAP Replace Script

Python script to automate the replacement or insertion of DXF blocks using the `ezdxf` library.

## What it does
The script reads an input DXF file from the `IN` directory (`IN/to_replace.dxf`), iterates through all block insertion entities (`INSERT`) present in the modelspace, and adds a specified new block (`new_block_name`) at the exact same `(x, y, z)` coordinates of each existing block. 

Optionally, it allows deleting the original blocks (`delete_old_blocks = True`) and saves the result as a new DXF file in the `OUT` directory (`OUT/replaced.dxf`).

## Dependencies
This script requires Python and the `ezdxf` library to manipulate DXF files.

You can install the dependency by running:
```bash
pip install ezdxf
```

## Configuration & Folders
The script automatically checks for and creates `IN` and `OUT` directories in the script's root folder if they do not exist.

Within `block_replace.py`, you can modify the following configuration parameters:
- `input_directory`: Directory for input DXF files (default: `"IN"`).
- `output_directory`: Directory for output DXF files (default: `"OUT"`).
- `input_file`: Path of the input DXF file (default: `os.path.join("IN", "to_replace.dxf")`).
- `output_file`: Path of the output DXF file (default: `os.path.join("OUT", "replaced.dxf")`).
- `new_block_name`: Name of the new block to insert (default: `"nap_placeholder"`).
- `new_layer_name`: Layer where the new block will be inserted (default: `"0"`).
- `delete_old_blocks`: Boolean (`True` or `False`). If `True`, deletes original blocks after inserting new ones.

## How to Run
Ensure you have installed the `ezdxf` dependency, place your input DXF inside the `IN` folder, and run the script with:

```bash
python block_replace.py
```
*(Or the equivalent command for your Python environment, such as `py block_replace.py`)*

## Relevant Information
- Automatically creates `IN` and `OUT` directories if they are missing.
- Performs an initial sanity check to ensure the new block (`new_block_name`) exists in the drawing's block definitions before processing insertions.
- Upon completion, prints the total count of processed/replaced blocks to the console.
