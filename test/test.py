# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure

@cocotb.test()
async def test_tt_um_senolgulgonul(dut):
    expected_letters = [
        "01011011",  # S
        "01001111",  # E
        "00010101",  # n
        "01111110",  # O
        "00001110",  # L
        "01011111",  # G
        "00111110",  # U
        "00001110",  # L
        "01011111",  # G
        "01111110",  # O
        "00010101",  # n
        "00111110",  # U
        "00001110",  # L
        "00000000"   # dp = 0
    ]

    # Ensure initialization
    dut.ui_in.value = 0

    # Wait for initialization to settle
    await Timer(500, units='ns')

    for i in range(len(expected_letters)):
        # Simulate button press: create a clean rising edge on ui_in[0]
        dut.ui_in.value = 0
        await Timer(100, units='ns')
        dut.ui_in.value = 1
        await Timer(100, units='ns')

        output_value = dut.uo_out.value.binstr  # Get the full 8-bit binary string

        dut._log.info(f'Index: {i}, Full Output: {output_value}')
        dut._log.info(f'Expected: {expected_letters[i]}, Actual: {output_value}')

        assert output_value == expected_letters[i], f"Mismatch at index {i}: Expected {expected_letters[i]}, got {output_value}"

        # Ensure ui_in[0] is low again for the next cycle
        dut.ui_in.value = 0
        await Timer(100, units='ns')

    dut._log.info("Test completed successfully.")

