module intcheck (
	input clk,    
	input reset, 
	input[7:0] in,  
	output out
);
reg[3:0] status;
reg o = 1'b0;
always @(posedge clk) begin 
	if(reset) begin
		status <= 0;
		 o <= 1'b0;
	end 
	else begin
		case (status)
			4'd0: begin
				if (in == "i") begin
					status <= 4'd1;
					o <= 1'b0;
				end
				else if (in == " " || in == "\t") begin
					status <= status;
					o <= 1'b0;
				end
				else if (in == ";") begin
					status <= status;
					o <= 1'b0;
				end
				else begin
					status <= 4'd12;
					o <= 1'b0;
				end
			end
			4'd1: begin
				if (in == "n") begin
					status <= 4'd2;
					o <= 1'b0;
				end
				else if (in == " " || in == "\t") begin
					status <= 4'd0;
					o <= 1'b0;
				end
				else begin
					status <= 4'd12;
					o <= 1'b0;
				end
			end
			4'd2: begin
				if (in == "t") begin
					status <= 4'd3;
					o <= 1'b0;
				end
				else if (in == ";") begin
					status <= 4'd0;
					o <= 1'b0;
				end
				else begin
					status <= 4'd12;
					o <= 1'b0;
				end
			end
			4'd3: begin
				if (in == " " || in == "\t") begin
					status <= 4'd4;
					o <= 1'b0;
				end
				else if (in == ";") begin
					status <= 4'd0;
					o <= 1'b0;
				end
				else begin
					status <= 4'd12;
					o <= 1'b0;
				end
			end
			4'd4: begin
				if (in == " " || in == "\t") begin
					status <= 4'd4;
					o <= 1'b0;
				end
				else if (in == "i") begin
					status <= 4'd5;
					o <= 1'b0;
				end
				else if ((in >= "a" && in <= "z") || (in >= "A" && in <= "Z") || (in == "_") || (in == "\0") || (in == "\t")) begin
					status <= 4'd8;
					o <= 1'b0;
				end
				else if (in == ";") begin
					status <= 4'd0;
					o <= 1'b0;
				end
				else begin
					status <= 4'd12;
					o <= 1'b0;
				end
			end
			4'd5: begin
				if (in == "n") begin
					status <= 4'd6;
					o <= 1'b0;
				end
				else if ((in >= "a" && in <= "z") || (in >= "A" && in <= "Z") || (in == "_") || (in == "\0") || (in == "\t") || (in >= "0" && in <= "9")) begin
					status <= 4'd8;
					o <= 1'b0;					
				end
				else if (in == ";") begin
					status <= 4'd0;
					o <= 1'b1;
				end
				else if (in == " " || in == "\t") begin
					status <= 4'd9;
					o <= 1'b0;
				end
				else if (in == ",") begin
					status <= 4'd4;
					o <= 1'b0;
				end
				else begin
					status <= 4'd12;
					o <= 1'b0;
				end
			end
			4'd6: begin
				if (in == "t") begin
					status <= 4'd7;
					o <= 1'b0;
				end
				else if ((in >= "a" && in <= "z") || (in >= "A" && in <= "Z") || (in == "_") || (in == "\0") || (in == "\t") || (in >= "0" && in <= "9")) begin
					status <= 4'd8;
					o <= 1'b0;					
				end
				else if (in == ";") begin
					status <= 4'd0;
					o <= 1'b1;
				end
				else if (in == " " || in == "\t") begin
					status <= 4'd9;
					o <= 1'b0;
				end
				else if (in == ",") begin
					status <= 4'd4;
					o <= 1'b0;
				end
				else begin
					status <= 4'd12;
					o <= 1'b0;
				end
			end
			4'd7: begin
				if ((in >= "a" && in <= "z") || (in >= "A" && in <= "Z") || (in == "_") || (in == "\0") || (in == "\t") || (in >= "0" && in <= "9")) begin
					status <= 4'd8;
					o <= 1'b0;
				end
				else if (in == ";") begin
					status <= 4'd0;
					o <= 1'b0;
				end
				else begin
					status <= 4'd12;
					o <= 1'b0;
				end
			end
			4'd8: begin
				if (in == " " || in == "\t") begin
					status <= 4'd9;
					o <= 1'b0;
				end
				else if (in == ",") begin
					status <= 4'd4;
					o <= 1'b0;
				end
				else if (in == ";") begin
					status <= 4'd0;
					o <= 1'b1;
				end
				else if ((in >= "a" && in <= "z") || (in >= "A" && in <= "Z") || (in == "_") || (in == "\0") || (in == "\t") || (in >= "0" && in <= "9")) begin
					status <= status;
					o <= 1'b0;
				end
				else begin
					status <= 4'd12;
					o <= 1'b0;
				end
			end
			4'd9: begin
				if (in == " " || in == "\t") begin
					status <= status;
					o <= 1'b0;
				end
				else if (in == ";") begin
					status <= 4'd0;
					o <= 1'b1;
				end
				else if (in == ",") begin
					status <= 4'd4;
					o <= 1'b0;
				end
				else begin
					status <= 4'd12;
					o <= 1'b0;
				end
			end
			4'd12: begin
				if (in == ";") begin
					status <= 4'd0;
					o <= 1'b0;
				end
				else begin
					status <= status;
					o <= 1'b0;
				end
			end
		endcase
	end
end
assign out = o;

endmodule 