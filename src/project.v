/*
 * Copyright (c) 2024 Senol Gulgonul
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

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
    reg [6:0] letters[0:12];

    initial begin
        // 7-segment encodings for "SEnOLGULGONUL"
        letters[0]  = 7'b1011011; // S
        letters[1]  = 7'b1001111; // E
        letters[2]  = 7'b0010101; // n
        letters[3]  = 7'b1111110; // O
        letters[4]  = 7'b0001110; // L
        letters[5]  = 7'b1011111; // G
        letters[6]  = 7'b0111110; // U
        letters[7]  = 7'b0001110; // L
        letters[8]  = 7'b1011111; // G
        letters[9]  = 7'b1111110; // O
        letters[10] = 7'b0010101; // n
        letters[11] = 7'b0111110; // U
        letters[12] = 7'b0001110; // L
        index = 0;
    end

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            index <= 0;
        else if (ui_in[0])  // Use the first bit of ui_in as the button input
            index <= (index == 4'd12) ? 0 : index + 1;

        {uo_out[6], uo_out[5], uo_out[4], uo_out[3], uo_out[2], uo_out[1], uo_out[0]} <= letters[index];
        uo_out[7] <= 1'b0; // Set the highest bit to 0
    end

    // Assign the other outputs
    assign uio_out = 8'b0;
    assign uio_oe = 8'b11111111;

    // Prevent warnings for unused inputs
    wire _unused = &{ena, uio_in, 1'b0};

endmodule


