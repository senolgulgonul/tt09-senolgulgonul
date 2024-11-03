/*
 * Copyright (c) 2024 Senol Gulgonul
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_senolgulgonul(
    input btn,
    output reg a, b, c, d, e, f, g
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

    always @(posedge btn) begin
        index <= index + 1;
        if (index == 4'd13) // Loop back after the last letter
            index <= 0;
        {a, b, c, d, e, f, g} <= letters[index];
    end

endmodule

