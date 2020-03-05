# Check if x is initialized
if is(x, symbol) then x := 10 end if: 
cat("x = ", x);

# Define firstprimes(n) function
firstprimes := n -> seq(ithprime(i), i = 1..n);

# Print function call and result
'firstprimes(x)';%;

quit()
