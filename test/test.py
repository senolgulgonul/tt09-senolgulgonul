# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_tt_um_senolgulgonul(dut):
    # Create a clock signal on dut.clk
    clock = Clock(dut.clk, 20, units="ns")  # 50 MHz clock
    cocotb.start_soon(clock.start())

    expected_letters = [
        "10000000",  # dp = 1
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
        "00001110"   # L
    ]

    # Initially set rst_n to 1
    dut.rst_n.value = 1
    await Timer(100, units='ns')
    
    # Apply reset by setting rst_n to 0
    dut.rst_n.value = 0
    await Timer(100, units='ns')
    
    # Release reset by setting rst_n to 1
    dut.rst_n.value = 1

    # Initialize all bits of dut.ui_in to 0
    dut.ui_in.value = 0

    for i in range(len(expected_letters)):
        await RisingEdge(dut.clk)  # Wait for the positive edge of the clock

        output_value = dut.uo_out.value.binstr  # Get the full 8-bit binary string

        dut._log.info(f'Index: {i}, Full Output: {output_value}')
        dut._log.info(f'Expected: {expected_letters[i]}, Actual: {output_value}')

        assert output_value == expected_letters[i], f"Mismatch at index {i}: Expected {expected_letters[i]}, got {output_value}"

    dut._log.info("Test completed successfully.")
