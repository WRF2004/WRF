module FDreg(
    input clk,
    input reset,
    input [31:0] f_instr,
    input [31:0] f_pc,
    input fd_stall,
    output reg [31:0] d_instr,
    output reg [31:0] d_pc
    );
    initial begin
        d_instr = 0;
    end 
    always @(posedge clk) begin
        if (reset) begin
            d_instr <= 0;
            d_pc <= 32'h00003000;
        end
        else if(!fd_stall) begin
            d_instr <= f_instr;
            d_pc <= f_pc;
        end
    end
endmodule