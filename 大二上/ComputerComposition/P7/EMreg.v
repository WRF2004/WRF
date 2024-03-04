module EMreg (
    input clk,
    input reset,
	 input eret,
	 input req,
	 input e_bd,
    input [4:0] e_a3,
	 input [4:0] em_exc,
    input [31:0] e_aluout,
    input [31:0] e_pc,
    input [31:0] e_instr,
    input [31:0] e_DMinput,
	 input [31:0] em_out,
	 input em_stall,
    
	 output reg [4:0] m_exc,
	 output reg m_bd,
    output reg [4:0] m_a3,
    output reg [31:0] m_aluout,
    output reg [31:0] m_pc,
    output reg [31:0] m_instr,
	 output reg [31:0] m_out,
    output reg [31:0] m_DMinput 
);
    
    always @(posedge clk) begin
        if (reset || em_stall || eret || req) begin
            m_a3 <= 0;
            m_aluout <= 0;
            m_pc <= 32'h00003000;
            m_instr <= 0;
            m_DMinput <= 0;
				m_out <= 0;
				m_bd <= 0;
				m_exc <= 0;
        end
        else begin
            m_a3 <= e_a3;
            m_aluout <= e_aluout;
            m_pc <= e_pc;
            m_instr <= e_instr;
            m_DMinput <= e_DMinput;
				m_out <= em_out;
				m_bd <= e_bd;
				m_exc <= em_exc;
        end
    end
endmodule