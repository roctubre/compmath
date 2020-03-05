# Check arguments
c := `if`(is(c, symbol), 3, c):
k := `if`(is(k, symbol), 2, k):
cat("c = ", c);
cat("k = ", k);

# Define functions
my_generalized_binomial := (`c`, `k`) ->  mul((`c`-`k`+1)..`c`) / mul(1..`k`);

# Print function call and result
'my_generalized_binomial(c, k)';
%;

quit()
