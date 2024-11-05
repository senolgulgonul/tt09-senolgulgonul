/*
 * Copyright (c) 2024 Senol Gulgonul
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_senolgulgonul (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

    reg [3:0] index;

    always @(posedge ui_in[0]) begin
        index <= (index == 4'd13) ? 0 : index + 1;
    end

    assign uo_out = (index == 4'd0)  ? 8'b10000000 : // dp = 1
                    (index == 4'd1)  ? 8'b01011011 : // S
                    (index == 4'd2)  ? 8'b01001111 : // E
                    (index == 4'd3)  ? 8'b00010101 : // n
                    (index == 4'd4)  ? 8'b01111110 : // O
                    (index == 4'd5)  ? 8'b00001110 : // L
                    (index == 4'd6)  ? 8'b01011111 : // G
                    (index == 4'd7)  ? 8'b00111110 : // U
                    (index == 4'd8)  ? 8'b00001110 : // L
                    (index == 4'd9)  ? 8'b01011111 : // G
                    (index == 4'd10) ? 8'b01111110 : // O
                    (index == 4'd11) ? 8'b00010101 : // n
                    (index == 4'd12) ? 8'b00111110 : // U
                    (index == 4'd13) ? 8'b00001110 : // L
                                       8'b00000000; // default

    // Assign the other outputs
    assign uio_out = 8'b0;
    assign uio_oe = 8'b11111111;

    // Prevent warnings for unused inputs
    wire _unused = &{ena, clk, rst_n, uio_in, ui_in[7:1]};

endmodule
