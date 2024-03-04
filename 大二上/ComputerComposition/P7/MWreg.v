 module MWreg (
    input clk,
    input reset,
    input [4:0] m_a3,
    input [31:0] mw_out,
    input [31:0] m_instr,
    input [31:0] m_pc,
    output reg [4:0] w_a3,
    output reg [31:0] w_out,
    output reg [31:0] w_instr,
    output reg [31:0] w_pc
);
    initial begin
        w_a3 = 0;
        w_out = 0;
        w_instr = 0;
        w_pc = 32'h00003000;
    end
    always @(posedge clk) begin
        if (reset) begin
            w_a3 <= 0;
            w_out <= 0;
            w_instr <= 0;
            w_pc <= 32'h00003000;
        end
        else begin
            w_a3 <= m_a3;
            w_out <= mw_out;
            w_instr <= m_instr;
            w_pc <= m_pc;
        end
    end
endmodule