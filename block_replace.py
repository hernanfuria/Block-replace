import os
import ezdxf

# -----------------------------
# Configuration
# -----------------------------
# Define input and output directory paths relative to the script location
input_directory = "IN"
output_directory = "OUT"

# Ensure that the input and output directories exist; create them if they do not
os.makedirs(input_directory, exist_ok=True)
os.makedirs(output_directory, exist_ok=True)

# Flag to determine whether original blocks should be deleted after insertion
delete_old_blocks = False  # Set to True to remove original blocks
new_layer_name = "0"       # Layer where the new block will be placed


# -----------------------------
# Batch Processing DXF Files
# -----------------------------
def main():
    """
    Main function to scan the IN directory for DXF files, interactively prompt 
    the user to select a replacement block for each file, process the replacements, 
    and save the output files into the OUT directory.
    """
    # Retrieve all files in the IN directory
    if not os.path.exists(input_directory):
        print(f"Directory '{input_directory}' does not exist.")
        return

    all_files = os.listdir(input_directory)
    # Filter for DXF files (case-insensitive extension check)
    dxf_files = [f for f in all_files if f.lower().endswith(".dxf")]

    if not dxf_files:
        print(f"No DXF files found in the '{input_directory}' directory.")
        return

    print(f"Found {len(dxf_files)} DXF file(s) in '{input_directory}'.\n")

    # Iterate through each DXF file found in the IN directory
    for filename in dxf_files:
        input_file_path = os.path.join(input_directory, filename)
        output_file_path = os.path.join(output_directory, filename)

        print(f"--------------------------------------------------")
        print(f"Processing file: {filename}")
        print(f"--------------------------------------------------")

        try:
            # Load the DXF drawing
            doc = ezdxf.readfile(input_file_path)
            msp = doc.modelspace()
        except Exception as e:
            print(f"Error reading DXF file '{filename}': {e}")
            continue

        # Collect unique block names referenced in the modelspace
        referenced_blocks = sorted(list({insert.dxf.name for insert in msp.query("INSERT")}))

        if not referenced_blocks:
            print(f"No block insertions ('INSERT') found in '{filename}'. Skipping.")
            # Even if no blocks, should we copy it or skip? Let's save as-is or skip. Let's skip or save.
            continue

        # Display numbered list of blocks found in the current drawing
        print("Available blocks found in modelspace:")
        for idx, block_name in enumerate(referenced_blocks, start=1):
            print(f"  [{idx}] {block_name}")

        # Prompt the user to select the replacement block by number
        selected_index = None
        while selected_index is None:
            try:
                user_input = input(f"Select the number of the block to use for replacement (1-{len(referenced_blocks)}): ")
                idx = int(user_input.strip())
                if 1 <= idx <= len(referenced_blocks):
                    selected_index = idx - 1
                else:
                    print(f"Invalid selection. Please enter a number between 1 and {len(referenced_blocks)}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        new_block_name = referenced_blocks[selected_index]
        print(f"Selected replacement block: '{new_block_name}'")

        # Sanity check: Ensure that the selected block definition exists in the drawing
        if new_block_name not in doc.blocks:
            print(f"Error: Block definition '{new_block_name}' not found in drawing blocks. Skipping.")
            continue

        count = 0

        # Iterate through all block insertion entities ('INSERT') in the modelspace
        for insert in msp.query("INSERT"):
            # Extract the 3D insertion coordinates (x, y, z) of the current block
            x, y, z = insert.dxf.insert

            # Create a new block reference at the exact same coordinates on the specified layer
            msp.add_blockref(
                new_block_name,
                (x, y, z),
                dxfattribs={"layer": new_layer_name},
            )

            # Increment the processed block counter
            count += 1

            # Optionally delete the old block entity if enabled in configuration
            if delete_old_blocks:
                msp.delete_entity(insert)

        # Save the modified drawing to the output path within the OUT directory
        doc.saveas(output_file_path)
        print(f"Successfully processed {count} block(s). Saved to '{output_file_path}'.\n")

    print("Batch processing completed for all files.")


if __name__ == "__main__":
    main()
