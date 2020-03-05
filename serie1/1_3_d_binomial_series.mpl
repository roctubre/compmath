# d) binomial series
# Converges if |x| < 1 and diverges if |x| >= 1
# if c >= 0, it expands the expression as a polynomial with c terms
n := `if`(is(n, symbol), infinity, n);
sum(binomial(c, k)*x^k, k=1..n);

# mul() can't take symbolic products.
#my_generalized_binomial := (`c`, `k`) ->  mul((`c`-`k`+1)..`c`) / mul(1..`k`):

my_generalized_binomial := (`c`, `k`) -> product(i, i=(`c`-`k`+1)..`c`) / product(j, j=1..`k`):
sum(my_generalized_binomial(c, k)*x^k, k=1..n);
simplify(%);
