4 < 5
10 > 100
4 == 6
5 == 5
5 != 4
5 ! 5
task1 <- !(10<5)
task1

task2 <- -10 > 10
task2

task1 | task2
task1 & task2

MyVector <- c(2,4,6,55,33)
MyVector
is.numeric(MyVector)
is.integer(MyVector)
is.double(MyVector)
vector_int <- c(2L, 44L, 55L)
is.integer(vector_int)
is.double(vector_int)

vector_char <- c("Shams", "Raaju", "Ahmed")
is.character(vector_char)

vector_mix <- c("Hello", "Print", 18)
is.character(vector_mix)
is.numeric(vector_mix)
1:15
seq(1,15)

new_seq <- seq(1, 20, 2)
new_seq
new_rep <- rep(4,5)
char_rep <- rep("Shams", 5)
char_rep
vec_rep <- c(22, 33, 56)
conv_vec <- rep(vec_rep, 5)
conv_vec
