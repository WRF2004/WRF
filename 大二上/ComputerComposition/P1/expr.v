module expr(
	input clk,
	input clr,
	input[7:0] in,
	output out
	);
reg[1:0] state;

always @(posedge clk or posedge clr) 
begin
	if (clr) begin
		state <= 2'd0;	
	end
	else begin
		case (state) 
			2'd0: begin
				if (in >= "0" && in <= "9") begin
					state <= 2'd2;
				end
				else begin
					state <= 2'd1;
				end
			end
			2'd1: begin
				state <= state;
			end
			2'd2: begin
				if (in == "+" || in == "*") begin
					state <= 2'd3;
				end
				else begin
					state <= 2'd1;
				end
			end
			2'd3: begin
				if (in >= "0" && in <= "9") begin
					state <= 2'd2;
				end
				else begin
					state <= 2'd1;
				end
			end
		endcase 
	end
end
assign out = (state == 2'd2) ? 1 : 0;

endmodule