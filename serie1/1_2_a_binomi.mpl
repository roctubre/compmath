# Check arguments
if is(n, symbol) then n := 10 end if:

# Define functions
my_binomi := (`a`, `b`, `n`) -> sum(binomial(`n`, k) * `a`^k * `b`^(`n`-k), k = 0 .. `n`);

# Print function call and result
'my_binomi(a, b, n)';
%;
'factor(my_binomi(a, b, n))';
%;

quit()
