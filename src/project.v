/*
 * Copyright (c) 2024 Senol Gulgonul
 * SPDX-License-Identifier: Apache-2.0
 */


`default_nettype none

module tt_um_senolgulgonul (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output reg [7:0] uo_out,    // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

    reg [3:0] index;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            index <= 4'd0;
            uo_out <= 8'b00000000;
        end else begin
            index <= (index == 4'd13) ? 0 : index + 1;
            case (index)
                4'd0:  uo_out <= 8'b10000000; // dp = 1
                4'd1:  uo_out <= 8'b01011011; // S
                4'd2:  uo_out <= 8'b01001111; // E
                4'd3:  uo_out <= 8'b00010101; // n
                4'd4:  uo_out <= 8'b01111110; // O
                4'd5:  uo_out <= 8'b00001110; // L
                4'd6:  uo_out <= 8'b01011111; // G
                4'd7:  uo_out <= 8'b00111110; // U
                4'd8:  uo_out <= 8'b00001110; // L
                4'd9:  uo_out <= 8'b01011111; // G
                4'd10: uo_out <= 8'b01111110; // O
                4'd11: uo_out <= 8'b00010101; // n
                4'd12: uo_out <= 8'b00111110; // U
                4'd13: uo_out <= 8'b00001110; // L
                default: uo_out <= 8'b00000000;
            endcase
        end
    end

    // Assign the other outputs
    assign uio_out = 8'b0;
    assign uio_oe = 8'b11111111;

    // Prevent warnings for unused inputs by logically AND-ing all bits and including a 0
    wire _unused = &{ena, uio_in, ui_in, 1'b0};

endmodule
