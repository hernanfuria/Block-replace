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

# Define full file paths for the source DXF and the processed output DXF
input_file = os.path.join(input_directory, "to_replace.dxf")
output_file = os.path.join(output_directory, "replaced.dxf")

# Name of the block to be inserted in place of existing ones
new_block_name = "nap_placeholder"  # Alternative: "NAP"

# Layer name where the new block will be placed
new_layer_name = "0"

# Flag to determine whether original blocks should be deleted after insertion
delete_old_blocks = False  # Set to True to remove original blocks


# -----------------------------
# Load Drawing
# -----------------------------
# Attempt to read the DXF drawing from the specified input path
doc = ezdxf.readfile(input_file)
msp = doc.modelspace()

# Sanity check: Ensure that the target new block definition exists in the drawing
if new_block_name not in doc.blocks:
    raise ValueError(f"Block '{new_block_name}' not found in drawing definitions.")

# Initialize counter for successfully processed block insertions
count = 0


# -----------------------------
# Find & Replace Blocks
# -----------------------------
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


# -----------------------------
# Save Drawing
# -----------------------------
# Save the modified drawing to the output path within the OUT directory
doc.saveas(output_file)

# Print confirmation message detailing total blocks processed
print(f"Successfully processed and replaced {count} blocks.")
