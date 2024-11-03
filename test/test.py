# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.triggers import RisingEdge
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
        dut.btn.value = 1
        await RisingEdge(dut.btn)
        await cocotb.triggers.Timer(1, units='ns')
        dut.btn.value = 0
        await cocotb.triggers.Timer(1, units='ns')
        
        output_value = (dut.a.value << 6) | (dut.b.value << 5) | (dut.c.value << 4) | \
                       (dut.d.value << 3) | (dut.e.value << 2) | (dut.f.value << 1) | \
                       (dut.g.value)
        dut._log.info(f'Index: {i}, Expected: {expected_letters[i]:07b}, Output: {output_value:07b}')
        
        if output_value != expected_letters[i]:
            raise TestFailure(f"Mismatch at index {i}: Expected {expected_letters[i]:07b}, got {output_value:07b}")

    dut._log.info("Test completed successfully.")

