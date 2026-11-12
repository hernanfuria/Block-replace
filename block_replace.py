import ezdxf

# -----------------------------
# configuration
# -----------------------------
input_file = r"to_replace.dxf"
output_file = r"replaced.dxf"

new_block_name = "nap_placeholder"#"NAP"
new_layer_name = "0"

delete_old_blocks = False   # change to True if you want to remove them


# -----------------------------
# load drawing
# -----------------------------
doc = ezdxf.readfile(input_file)
msp = doc.modelspace()

# sanity check: ensure new block exists
if new_block_name not in doc.blocks:
    raise ValueError(f"Block '{new_block_name}' not found in drawing.")

count = 0

# -----------------------------
# find & replace
# -----------------------------
for insert in msp.query("INSERT"):
    # print(insert.dxf.name, insert.dxf.layer)
    # if insert.dxf.name == old_block_name and insert.dxf.layer == old_layer_name:
    x, y, z = insert.dxf.insert
    # print(f"found {old_block_name} @ {x}, {y}")

    # create new insert
    msp.add_blockref(
        new_block_name,
        (x, y, z),
        dxfattribs={"layer": new_layer_name},
    )

    count += 1

    # optionally delete old one
    if delete_old_blocks:
        msp.delete_entity(insert)

# -----------------------------
# save
# -----------------------------
doc.saveas(output_file)

print(f"Replaced {count} blocks.")
