# Lesson 2: Variables and Data Types
# Python for Embedded Engineers

# 1. Variables declaration and initialization
reg_val     = 0xFF          # Hexadecimal value
adc_val     = 1023          # Decimal value
sys_tick    = 0xADCBDDFF    # Hexadecimal value of 32 bits
voltage     = 3.3           # Floating-point value
is_Active   = True          # Boolean value
mcu_name    = "ESP32"       # String value
reg         = 0b11001010    # Binary of value 0xCA

# Print variables
# print() function is used to print value of variable
print("Output -- Variable Values")
print(reg_val)
print(adc_val)
print(sys_tick)
print(voltage)
print(is_Active)
print(mcu_name)

# Check variable type
# type() function is used to check type of variables
# Input to type() function - variable name
print("Output -- Variable Type")
print(type(reg_val))
print(type(adc_val))
print(type(sys_tick))
print(type(voltage))
print(type(is_Active))
print(type(mcu_name))

# Print variables in formatted string format
# print(f". . . "") - prifix f tells Python to look inside the { }
print("Output - Variable values using formatted string")

#     f tells Python this   expression to evaluate
#     is formatted string   |
#     |                     |
print(f"reg_val     =       {reg_val}")
print(f"adc_val     =       {adc_val}")
print(f"sys_tick    =       {sys_tick}")
print(f"voltage     =       {voltage}")
print(f"is_Active   =       {is_Active}")
print(f"mcu_name    =       {mcu_name}")

# Bitwise Operation
print("Output -- Bitwise Operation")
print(f"Original value of reg   : 0x{reg:08b}")
print(f"Bitwise AND Operation   : 0x{(reg & 0x0F):08b}")    # Mask Lower Nibble
print(f"Bitwise OR Operation    : 0x{(reg | 1):08b}")       # Set 0th bit    
print(f"Bitwise EXOR Operation  : 0x{(reg ^ 0xFF):08b}")    # Toggle all bits
print(f"Bitwise Inversion       : 0x{(~reg & 0xFF):08b}")   # Invert all bits
print(f"Left Shift Operation    : 0x{(reg << 2):08b}")      # Left shift by 2 position
print(f"Right Shift Operation   : 0x{(reg >> 2):08b}")      # Right shift by 2 position       