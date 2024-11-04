# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0
import os
import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure

# Set the environment variable
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

    dut.ui_in.value = 0

    for i in range(len(expected_letters)):
        # Simulate button press: create a rising edge on ui_in[0]
        dut.ui_in.value = 1
        await Timer(1, units='ns')
        dut.ui_in.value = 0
        await Timer(1, units='ns')

        output_value = dut.uo_out.value.binstr[-7:]  # Get the lower 7 bits in binary
        dut._log.info(f'Index: {i}, Expected: {expected_letters[i]}, Output: {output_value}')

        if output_value != expected_letters[i]:
            raise TestFailure(f"Mismatch at index {i}: Expected {expected_letters[i]}, got {output_value}")

    dut._log.info("Test completed successfully.")


