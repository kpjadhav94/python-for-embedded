# Exercise -- Variables and Data Types

# Create variables and assign values to them.
# Create variables of different data types - int, float, bool, string

reg_addr        = 0x40020000        # GPIO base address
reg_val         = 0xCA              # Register value
pin_mask        = 0b00000001        # Pin 0 mask
baud_rate       = 115200            # UART baud rate
voltage         = 3.3               # MCU supply voltage
mcu_name        = "STM32F407"       # MCU name
is_ready        = True              # Status flag

# Print variable type
print("Formatted Output -- Variable Type")
print(f"The type of reg_addr    : {type(reg_addr)}")
print(f"The type of reg_val     : {type(reg_val)}")
print(f"The type of pin_mask    : {type(pin_mask)}")
print(f"The type of baud_rate   : {type(baud_rate)}")
print(f"The type of voltage     : {type(voltage)}")
print(f"The type of mcu_name    : {type(mcu_name)}")
print(f"The type of is_ready    : {type(is_ready)}")

# Print variable values
print("\nFormatted Output -- Variable Values")
print(f"reg_addr    = 0x{reg_addr:08X}")
print(f"reg_val     = 0x{reg_val:02X}")
print(f"pin_mask    = 0b{pin_mask:08b}")
print(f"baud_rate   = {baud_rate} bps")
print(f"voltage     = {voltage:.1f}V")
print(f"mcu_name    = {mcu_name}")
print(f"is_ready    = {is_ready}\n")

# Bitwise Operations
print("Output -- Bitwise Operation of variables")
print(f"AND mask    : 0b{reg_val & 0x0F:08b}")
print(f"TOGGLE Bit1 : 0b{reg_val ^ 0xFF:08b}")
print(f"Set Bit4    : 0b{reg_val | 0x10:08b}")
print(f"NOT         : 0b{~reg_val & 0xFF:08b}")
print(f"LSH << 2    : 0b{reg_val << 2:10b}")
print(f"RSH >> 2    : 0b{reg_val >> 2:08b}")