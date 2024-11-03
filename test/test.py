# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.triggers import RisingEdge, FallingEdge
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

    for i in range(len(expected_letters)):
        dut.ui_in.value = 1
        await RisingEdge(dut.clk)
        await FallingEdge(dut.clk)
        dut.ui_in.value = 0
        await RisingEdge(dut.clk)
        await FallingEdge(dut.clk)
        
        output_value = (dut.uo_out.value << 6) | (dut.uio_out.value << 5) | (dut.uio_oe.value << 4) | \
                       (dut.uio_oe.value << 3) | (dut.uio_oe.value << 2) | (dut.uio_oe.value << 1) | \
                       (dut.uio_oe.value)
        dut._log.info(f'Index: {i}, Expected: {expected_letters[i]:07b}, Output: {output_value:07b}')
        
        if output_value != expected_letters[i]:
            raise TestFailure(f"Mismatch at index {i}: Expected {expected_letters[i]:07b}, got {output_value:07b}")

    dut._log.info("Test completed successfully.")


