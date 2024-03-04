.data
    symbol: .space 28
    array: .space 28

.macro end
    li      $v0, 10
    syscall
.end_macro

.macro getInt(%des)
    li      $v0, 5
    syscall
    move    %des, $v0
.end_macro

.macro print(%out)
    li $v0, 1
    move $a0, %out
    syscall
.end_macro

.macro println()
    li $v0, 11
    li $a0, '\n'
    syscall
.end_macro

.macro printspace()
    li $v0, 11
    li $a0, ' '
    syscall
.end_macro

.macro push(%src)
    sw      %src, 0($sp)
    subi    $sp, $sp, 4
.end_macro

.macro pop(%des)
    addi    $sp, $sp, 4
    lw      %des, 0($sp) 
.end_macro

.text
    getInt($t0)         # $t0 = n
    li $a0, 0            # index
    jal Full
    end
    
Full:
    push($ra)
    push($t1)
    push($t2)
    
    move $t2, $a0        # $t2 = index
    move $t1, $zero
    bgt $t0, $t2, for_1 # index < n 

for_2:
    sll $t3, $t1, 2
    lw $t4, array($t3)
    print($t4)
    printspace()
    addi $t1, $t1, 1
    bne $t1, $t0, for_2

    println()

    pop($t2)
    pop($t1)
    pop($ra)
    jr $ra

for_1:
    sll $t3, $t1, 2
    lw $t4, symbol($t3)
    beq $t4, $zero, if_2  # 如果 symbol[i] == 0 则跳转到 if_2
    addi $t1, $t1, 1
    bne $t1, $t0, for_1

if_2:
    sll $t3, $t2, 2
    addi $t4, $t1, 1
    sw $t4, array($t3)  # array[index] = i + 1
    sll $t3, $t1, 2
    li $t4, 1
    sw $t4, symbol($t3)  # symbol[i] = 1
    addi $a0, $t2, 1
    jal Full            # Full[index+1]
    subi $a0, $t2, 1     # 回溯时将index减1
    sll $t3, $t1, 2
    sw $zero, symbol($t3)  # symbol[i] = 0
    addi $t1, $t1, 1
    bne $t1, $t0, for_1