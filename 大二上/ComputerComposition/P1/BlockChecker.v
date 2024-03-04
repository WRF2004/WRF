module BlockChecker (
	input clk,    // Clock
	input reset, // Clock Enable
	input[7:0] in,  // Asynchronous reset active low
	output result
);
reg[4:0] status;
reg[31:0] count;
reg flag = 1'b0;

always @(posedge clk or posedge reset) begin
	if (reset) begin
		status <= 5'd0;
		count <= 0;
		flag <= 0;
	end 
	else begin
		case (status)
			5'd0: begin
				if (in == "b" || in == "B") begin
					status <= 5'd1;
					count <= count;
				end
				else if (in == "e" || in == "E") begin
					status <= 5'd6;
					count <= count;
				end
				else if (in == " ") begin
					status <= status;
					count <= count;
				end
				else begin
					status <= 5'd9;
				end
			end
			5'd1: begin
				if (in == "e" || in == "E") begin
					status <= 5'd2;
					count <= count;
				end
				else if (in == " ") begin
					status <= 5'd0;
					count <= count;
				end
				else begin
					status <= 5'd9;
					count <= count;
				end
			end
			5'd2: begin
				if (in == "g" || in == "G") begin
					status <= 5'd3;
					count <= count;
				end
				else if (in == " ") begin
					status <= 5'd0;
					count <= count;
				end
				else begin
					status <= 5'd9;
					count <= count;
				end
			end
			5'd3: begin
				if (in == "i" || in == "I") begin
					status <= 5'd4;
					count <= count;
				end
				else if (in == " ") begin
					status <= 5'd0;
					count <= count;
				end
				else begin
					status <= 5'd9;
					count <= count;
				end
			end
			5'd4: begin
				if (in == "n" || in == "N") begin
					status <= 5'd5;
					count <= count + 1;
				end
				else if (in == " ") begin
					status <= 5'd0;
					count <= count;
				end
				else begin
					status <= 5'd9;
					count <= count;
				end
			end
			5'd5: begin
				if (in == " ") begin
					status <= 5'd0;
					count <= count;
				end
				else begin
					status <= 5'd9;
					count <= count - 1;
				end
			end
			5'd6: begin
				if (in == "n" || in == "N") begin
					status <= 5'd7;
					count <= count;
				end
				else if (in == " ") begin
					status <= 5'd0;
					count <= count;
				end
				else begin
					status <= 5'd9;
					count <= count;
				end
			end
			5'd7: begin
				if (in == " ") begin
					count <= count;
					status <= 5'd0;
				end
				else if ((in == "d" || in == "D") && count != 0) begin
					status <= 5'd8;
					count <= count - 1;
				end
				else if ((in == "d" || in == "D") && count == 0) begin
					status <= 5'd10;
					count <= count;
					flag <= 1;
				end
				else begin
					count <= count;
					status <= 5'd9;
				end
			end
			5'd8: begin
				if (in == " ") begin
					status <= 5'd0;
					count <= count;
				end
				else begin
					count <= count + 1;
					status <= 5'd9;
				end
			end
			5'd9: begin
				if (in == " ") begin
					status <= 5'd0;
					count <= count;
				end
				else begin
					status <= status;
					count <= count;
				end
			end
			5'd10: begin
				if (in == " ") begin
					flag <= 1;
					status <= 5'd11;
				end
				else begin
					flag <= 0;
					count <= count;
					status <= 5'd9;
				end
			end
			5'd11: begin
				status <= status;
				flag <= 1;
				count <= count;
			end
		endcase // status
	end
end
assign result = (count == 0 && flag == 0) ? 1 : 0;

endmodule