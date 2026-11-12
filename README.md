# Block Replace Script

Python script to automate the batch replacement or insertion of DXF blocks using the `ezdxf` library.

## What it does
- Scans the `IN` directory for all `.dxf` files.
- Automatically creates `IN` and `OUT` directories if they do not exist.
- For each DXF file found:
  - Inspects all block insertion entities (`INSERT`) present in the modelspace.
  - Displays an interactive numbered list of available blocks.
  - Prompts the user to select which block to use as the replacement (`new_block_name`).
  - Adds the selected new block at the exact same `(x, y, z)` coordinates of each existing block.
  - Optionally deletes original blocks (`delete_old_blocks = True`).
  - Saves the processed result into the `OUT` directory keeping the original filename.

## Dependencies
This script requires Python and the `ezdxf` library to manipulate DXF files.

You can install the dependency by running:
```bash
pip install ezdxf
```

## Configuration & Usage
Within `block_replace.py`, you can modify:
- `input_directory`: Directory for input DXF files (default: `"IN"`).
- `output_directory`: Directory for output DXF files (default: `"OUT"`).
- `new_layer_name`: Layer where the new block will be inserted (default: `"0"`).
- `delete_old_blocks`: Boolean (`True` or `False`). If `True`, deletes original blocks after inserting new ones.

## How to Run
1. Place one or more DXF files into the `IN` folder.
2. Execute the script either by double-clicking `run.bat` or running in your terminal:
   - Using the batch script: double-click `run.bat`
   - Using Python directly:
     ```bash
     python block_replace.py
     ```
     *(Or `py block_replace.py`)*

3. Follow the interactive prompts in the console to select the replacement block for each file.
