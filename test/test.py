# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import os
import cocotb
from cocotb.triggers import Timer

# Ensure environment variable is set to ignore 'x' states
os.environ["COCOTB_RESOLVE_X"] = "IGNORE"

@cocotb.test()
async def test_tt_um_senolgulgonul(dut):
    expected_letters = [
        "1011011",  # S
        "1001111",  # E
        "0010101",  # n
        "1111110",  # O
        "0001110",  # L
        "1011111",  # G
        "0111110",  # U
        "0001110",  # L
        "1011111",  # G
        "1111110",  # O
        "0010101",  # n
        "0111110",  # U
        "0001110"   # L
    ]

    # Ensure initialization
    dut.ui_in.value = 0

    # Long initialization period to settle all signals
    await Timer(500, units='ns')

    for i in range(len(expected_letters)):
        # Simulate button press: create a clean rising edge on ui_in[0]
        dut.ui_in.value = 0
        await Timer(50, units='ns')
        dut.ui_in.value = 1
        await Timer(50, units='ns')

        full_output = dut.uo_out.value.binstr  # Get the full binary string
        output_value = full_output[7:1]  # Correctly slice the lower 7 bits in binary
        
        dut._log.info(f'Index: {i}, Full Output: {full_output}, Masked Output: {output_value}')
        dut._log.info(f'Expected: {expected_letters[i]}, Actual: {output_value}')

        if 'x' in full_output or 'z' in full_output:
            dut._log.warning(f"Unresolved state detected at index {i}: Full Output: {full_output}")

        assert output_value == expected_letters[i], f"Mismatch at index {i}: Expected {expected_letters[i]}, got {output_value}"

        dut.ui_in.value = 0
        await Timer(50, units='ns')

    dut._log.info("Test completed successfully.")

