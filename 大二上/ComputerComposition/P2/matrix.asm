.data
	matrix1: .word 0 : 64
	matrix2: .word 0 : 64
	matrix3: .word 0 : 64
	
.macro calc_addr(%dst, %row, %column, %rank)
    multu %row, %rank
    mflo %dst
    addu %dst, %dst, %column
    sll %dst, %dst, 2
.end_macro

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

.text
	getInt($t0)
	move $s0, $zero  # rows
	move $s1, $zero	 # columns
	move $t2, $zero	 # address
loop1:
	getInt($t2)
	calc_addr($s2, $s0, $s1, $t0)
	sw $t2, matrix1($s2)
	addi $s1, $s1, 1
	bne $s1, $t0, loop1
	move $s1, $zero
	addi $s0, $s0, 1
	bne $s0, $t0, loop1
	
	move $s0, $zero  # rows
	move $s1, $zero	 # columns
	move $t2, $zero	 # value
	
loop2:
	getInt($t2)
	calc_addr($s2, $s0, $s1, $t0)
	sw $t2, matrix2($s2)
	addi $s1, $s1, 1
	bne $s1, $t0, loop2
	move $s1, $zero
	addi $s0, $s0, 1
	bne $s0, $t0, loop2
	
	move $t2, $zero
	move $s0, $zero  # rows
	move $s1, $zero	 # columns
	move $t1, $zero
	move $t3, $zero
	move $t4, $zero
	move $t5, $zero
	
loop3:
	calc_addr($s2, $s0, $t1, $t0)
	lw $t2, matrix1($s2)
	calc_addr($s2, $t1, $s1, $t0)
	lw $t3, matrix2($s2)
	multu $t3, $t2
	mflo $t4
	add $t5, $t5, $t4
	addi $t1, $t1, 1
	bne $t1, $t0, loop3
	calc_addr($s2, $s0, $s1, $t0)
	sw $t5, matrix3($s2)
	move $t5, $zero 
	move $t1, $zero 
	addi $s1, $s1, 1
	bne $s1, $t0, loop3
	move $s1, $zero
	addi $s0, $s0, 1
	bne $s0, $t0, loop3
	
	move $t2, $zero
	move $s0, $zero  # rows
	move $s1, $zero	 # columns
	
loop4:
	calc_addr($s2, $s0, $s1, $t0)
	lw $t2, matrix3($s2)
	print($t2)
	printspace()
	addi $s1, $s1, 1
	bne $s1, $t0, loop4
	move $s1, $zero
	addi $s0, $s0, 1
	println()
	bne $s0, $t0, loop4
	
	end