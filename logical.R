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


names <- c("Shamsul", "Raaju", "Haque", "Ahmed")
name_rep <- rep(names, 2)
name_rep


words <- c("a", "b", "c", "d", "e", "f")
words[1]
words[1:5]
words[7]
words[0]
words[c(1,3,5)]
words
words[c(2,4,6)]
x <- rnorm(5)
for (i in x){
  print (i)
  i <=x
}

x <- c(1:5)
for (i in x){
  i <x
  print (i)
  
}
?rnorm()


greeting <- function(name = "Shams"){
  print(paste("Hello, ", name, "!", sep = ""))
}

greeting()
greeting("Raaju")

numbers <- function(...){
  convert_into_vector <- c(...)
  sum(convert_into_vector)
}

numbers(5, 10, 15)
numbers(1, 2, 3)

a <- sapply(1:5, function(x) x^2)

print(a)
---------------------------------------------------

new_func <- function (func, vector) {
  
  sapply(vector, func)
}

result <- new_func(function(x) x^2, 1:5)
print(result)

outer_func <- function(argument1) {
  
  function(argument2) {
    
    return(argument2 * argument1)
  }
  
}
x <- outer_func(3)
x(5)