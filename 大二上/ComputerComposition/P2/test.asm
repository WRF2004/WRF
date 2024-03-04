.data
	Char: .space 25
	
.macro getChar(%des)
	li $v0, 12
	syscall
	sb $v0, Char(%des)
.end_macro

.macro printChar(%des)
	li $v0, 11
	lb $a0, Char(%des)
	syscall
.end_macro

.macro getInt(%des)
	li $v0, 5
	syscall
	move %des, $v0
.end_macro

.macro end
	li $v0, 10
	syscall
.end_macro

.text
	getInt($t0)
	move $t1, $zero
	
loop:
	getChar($t1)
	addi $t1, $t1, 1
	bne $t1, $t0, loop
	
	addi $t1, $t1, -1
	
print:
	printChar($t1)
	addi $t1, $t1, -1
	bgez  $t1, print
	
	end