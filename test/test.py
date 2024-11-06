# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_tt_um_senolgulgonul(dut):
    # Create a clock signal on dut.clk
    clock = Clock(dut.clk, 100, units="ns")  # 100ns clock period (10 MHz clock)
    cocotb.start_soon(clock.start())

    expected_letters = [
        "00000000",  # blank
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

    # Apply reset by setting rst_n to 1, then to 0, wait for 10ns, then set rst_n to 1
    dut.rst_n.value = 1
    await Timer(10, units='ns')
    dut.rst_n.value = 0
    await Timer(10, units='ns')
    dut.rst_n.value = 1
    await Timer(10, units='ns')  # Add a delay after setting rst_n to 1

    i = 0
    while i < len(expected_letters):  # Loop until i reaches the length of expected_letters
        await RisingEdge(dut.clk)  # Wait for the positive edge of the clock

        output_value = dut.uo_out.value.binstr  # Get the full 8-bit binary string
        expected_value = expected_letters[i]

        dut._log.info(f'Index: {i}, Full Output: {output_value}')
        dut._log.info(f'Expected: {expected_value}, Actual: {output_value}')

        assert output_value == expected_value, f"Mismatch at index {i}: Expected {expected_value}, got {output_value}"
        
        i += 1  # Increment i

    dut._log.info("Test completed successfully.")
