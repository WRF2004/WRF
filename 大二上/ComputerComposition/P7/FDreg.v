module FDreg(
    input clk,
    input reset,
	 input eret,
	 input req,
	 input f_bd,
	 input [4:0] f_exc,
    input [31:0] f_instr,
    input [31:0] f_pc,
    input fd_stall,
    output reg [31:0] d_instr,
    output reg [31:0] d_pc,
	 output reg d_bd,
	 output reg [4:0] d_exc
    );
   
    always @(posedge clk) begin
        if (reset || req || eret) begin
            d_instr <= 0;
            d_pc <= 32'h00003000;
				d_bd <= 0;
				d_exc <= 0;
        end
        else if(!fd_stall) begin
            d_instr <= f_instr;
            d_pc <= f_pc;
				d_bd <= f_bd;
				d_exc <= f_exc;
        end
    end
endmodule