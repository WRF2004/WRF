module FloatType (
	input[31:0] num,    
	output[4:0] float_type
);
assign float_type = (num[30:23] == 8'b0000_0000 && num[22:0] == 23'b0) ? 5'b00001 :
					(num[30:23] == 8'b0000_0000) ? 5'b00100 : 
					(num[30:23] == 8'b1111_1111 && num[22:0] == 23'b0) ? 5'b01000 : 
					(num[30:23] == 8'b1111_1111) ? 5'b10000 : 5'b00010;

endmodule : FloatType