module PC(
	input clk,
	input reset,
	
	input [31:0] npc,
	
	input fd_stall,
	
	output reg [31:0] f_pc
    );
	initial begin
		f_pc = 32'h00003000;
	end
	always @(posedge clk) begin
		if (reset) begin
			f_pc <= 32'h00003000;
		end
		else if (!fd_stall) begin
			f_pc <= npc;
		end
	end

endmodule
