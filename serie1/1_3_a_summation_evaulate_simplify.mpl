# a) Evaluate sums and simplify
# The sum() function is a symbolic summation
# For finite series it is recommended to use add() -> see ? sum and ? add

sum(k, k=1..n); 
simplify(%);
sum(k^2, k=1..n);
simplify(%);
sum(k^3, k=1..n);
simplify(%);

sum(1/k, k=1..n);
simplify(%);
sum(1/k^2, k=1..n);
simplify(%);

sum(x^k, k=1..n);
simplify(%);
sum(k*x^k, k=1..n);
simplify(%);
sum(k^2*x^k, k=1..n);
simplify(%);
sum(k^p*x^k, k=1..n);
simplify(%);
