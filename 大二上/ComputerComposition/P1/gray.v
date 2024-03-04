module gray(
  input Clk,
  input Reset,
  input En,
  output [2:0] Output,
  output Overflow
);
reg[2:0] oc = 3'b000;
reg fc = 1'b0;

always @(posedge Clk) begin
  if (Reset) begin
    oc <= 3'b000;
    fc <= 0;
  end
  else begin 
  	if (En) begin
    	case (oc) 
        3'b000: begin
          oc <= 3'b001;
          fc <= fc;
        end
        3'b001: begin
          oc <= 3'b011;
          fc <= fc;
        end
        3'b011: begin
          oc <= 010;
          fc <= fc;
        end
        3'b010: begin
          oc <= 3'b110;
          fc <= fc;
        end
        3'b110: begin
          oc <= 3'b111;
          fc <= fc;
        end
        3'b111: begin
          oc <= 3'b101;
          fc <= fc;
        end
        3'b101: begin
          oc <= 3'b100;
          fc <= fc;
        end
        3'b100: begin
          oc <= 3'b000;
          fc <= 1'b1;
        end
      endcase
  	end
    else begin
      oc <= oc;
      fc <= fc;
    end
  end
end
assign Output = oc;
assign Overflow = fc;

endmodule