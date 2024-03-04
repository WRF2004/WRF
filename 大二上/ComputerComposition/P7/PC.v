module PC(
	input clk,
	input reset,
	
	input [31:0] pc_in,
	
	input en,
	
	output reg [31:0] pc_out
    );
	initial begin
		pc_out = 32'h00003000;
	end
	always @(posedge clk) begin
		if (reset) begin
			pc_out <= 32'h00003000;
		end
		else if (en) begin
			pc_out <= pc_in;
		end
	end

endmodule
