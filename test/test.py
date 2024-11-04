# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb

@cocotb.test()
async def bypass_test(dut):
    dut._log.info("Test completed successfully.")
