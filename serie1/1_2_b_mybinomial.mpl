# Check arguments
n := `if`(is(n, symbol), 3, n):
k := `if`(is(k, symbol), 2, k):
cat("n = ", n);
cat("k = ", k);

# Define functions
my_binomial := (`n`, `k`) -> `if`(`k`=`n`, 1, mul((`k`+1)..`n`) / mul(`n`-`k`));

# Print function call and result
'my_binomial(n, k)';
%;

quit()
