module DEreg (
    input clk,
    input reset,
    input [31:0] d_instr,
    input [31:0] ext_imm32d,
    input [31:0] d_pc,
    input [31:0] FW_d_d1,
    input [31:0] FW_d_d2,
    input [4:0] d_a3,
	 input [31:0] de_out,
	 
	 input de_stall,
	 input em_stall,

    output reg [4:0] e_a3,
    output reg [31:0] e_pc,
    output reg [31:0] e_rd1,
    output reg [31:0] e_rd2,
    output reg [31:0] e_instr,
    output reg [31:0] ext_imm32e,
	 output reg [31:0] e_out
);
    initial begin
        e_a3 = 0;
        e_pc = 32'h00003000;
        e_rd1 = 0;
        e_rd2 = 0;
        e_instr = 0;
        ext_imm32e = 0;
		  e_out = 0;
    end
    always @(posedge clk) begin
        if (reset || de_stall) begin
            e_a3 <= 0;
            e_pc <= 32'h00003000;
            e_rd1 <= 0;
            e_rd2 <= 0;
            e_instr <= 0;
            ext_imm32e <= 0;
				e_out <= 0;
        end
        else if (!em_stall) begin
            e_a3 <= d_a3;
            e_pc <= d_pc;
            e_rd1 <= FW_d_d1;
            e_rd2 <= FW_d_d2;
            e_instr <= d_instr;
            ext_imm32e <= ext_imm32d;
				e_out <= de_out;
        end
    end
endmodule