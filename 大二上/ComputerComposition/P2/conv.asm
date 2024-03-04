.data
	matrix1: .word 0 : 121
	matrix2: .word 0 : 121
	matrix3: .word 0 : 121
	
.macro calc_addr(%dst, %row, %column, %rank)
    multu %row, %rank
    mflo %dst
    addu %dst, %dst, %column
    sll %dst, %dst, 2
.end_macro
	
.macro end
    li $v0, 10
    syscall
.end_macro

.macro getInt(%des)
    li $v0, 5
    syscall
    move %des, $v0
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
	getInt($t1)
	getInt($t2)
	getInt($t3)
	
	move $s0, $zero  # rows
	move $s1, $zero	 # columns

loop1:
	getInt($t4)
	calc_addr($s2, $s0, $s1, $t1)
	sw $t4, matrix1($s2)
	addi $s1, $s1, 1
	bne $s1, $t1, loop1
	move $s1, $zero
	addi $s0, $s0, 1
	bne $s0, $t0, loop1
	
	move $s0, $zero  # rows
	move $s1, $zero	 # columns
	
loop2:
	getInt($t4)
	calc_addr($s2, $s0, $s1, $t3)
	sw $t4, matrix2($s2)
	addi $s1, $s1, 1
	bne $s1, $t3, loop2
	move $s1, $zero
	addi $s0, $s0, 1
	bne $s0, $t2, loop2
	
	move $s0, $zero  # i+k
	move $s1, $zero	 # j+l
	move $s2, $zero  # k
	move $s3, $zero	 # l
	move $t7, $zero  # sum
	move $s5, $zero  # i
	move $s6, $zero	 # j
	move $t4, $zero	 
	
loop3:
	add $s0, $s5, $s2
	add $s1, $s6, $s3
	calc_addr($s4, $s0, $s1, $t1)
	lw $t4, matrix1($s4)
	calc_addr($s4, $s2, $s3, $t3)
	lw $t5, matrix2($s4)
	multu $t4, $t5
	mflo $t6
	add $t7, $t7, $t6
	addi $s3, $s3, 1
	bne $s3, $t3, loop3
	move $s3, $zero
	addi $s2, $s2, 1
	bne $s2, $t2, loop3
	sub $t4, $t1, $t3
	addi $t4, $t4, 1
	calc_addr($s4, $s5, $s6, $t4)
	sw $t7, matrix3($s4)
	move $t7, $zero
	move $s2, $zero
	move $s3, $zero
	addi $s6, $s6, 1
	bne $s6, $t4, loop3
	sub $t5, $t0, $t2
	addi $t5, $t5, 1
	move $s6, $zero
	addi $s5, $s5, 1
	bne $s5, $t5, loop3
	
	sub $t4, $t1, $t3
	addi $t4, $t4, 1 
	sub $t5, $t0, $t2
	addi $t5, $t5, 1
	move $s0, $zero  
	move $s1, $zero	 
	
loop4:
	calc_addr($s2, $s0, $s1, $t4)
	lw $t6, matrix3($s2)
	print($t6)
	printspace()
	addi $s1, $s1, 1
	bne $s1, $t4, loop4
	move $s1, $zero
	addi $s0, $s0, 1
	println()
	bne $s0, $t5, loop4
	end