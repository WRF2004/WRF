module Writeback (
    input [31:0] w_instr,
    output w_we
);

    Controller w_ctrl (
    .instr(w_instr), 
    .we(w_we)
    );

endmodule