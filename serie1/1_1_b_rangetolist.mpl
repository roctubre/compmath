# Check if x is initialized
if is(intrange, symbol) then intrange := 1 .. 10 end if: 
cat("intrange = ", [intrange]);

# Define rangetolist(intrange) function
rangetolist := range -> [seq(i, i = range)];

# Print function call and result
'rangetolist(intrange)';%;

quit()
