# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure

@cocotb.test()
async def test_tt_um_senolgulgonul(dut):
    expected_letters = [
        0b1011011,  # S
        0b1001111,  # E
        0b0010101,  # n
        0b1111110,  # O
        0b0001110,  # L
        0b1011111,  # G
        0b0111110,  # U
        0b0001110,  # L
        0b1011111,  # G
        0b1111110,  # O
        0b0010101,  # n
        0b0111110,  # U
        0b0001110   # L
    ]

    dut.ui_in.value = 0

    for i in range(len(expected_letters)):
        # Manually trigger the positive edge of ui_in[0]
        dut.ui_in.value = 1
        await Timer(1, units='ns')  # Allow time for the positive edge to be recognized
        dut.ui_in.value = 0
        await Timer(1, units='ns')  # Allow time for the value to propagate

        output_value = dut.uo_out.value.integer & 0x7F  # Mask the highest bit
        dut._log.info(f'Index: {i}, Expected: {expected_letters[i]:07b}, Output: {output_value:07b}')
       
        if output_value != expected_letters[i]:
            raise TestFailure(f"Mismatch at index {i}: Expected {expected_letters[i]:07b}, got {output_value:07b}")

    dut._log.info("Test completed successfully.")

