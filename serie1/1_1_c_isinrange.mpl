# Check if variables are initialized
if is(k, symbol) then k := 3 end if:
if is(intrange, symbol) then intrange := 1 .. 10 end if: 
cat("k = ", k);
cat("intrange = ", [intrange]);

# Define functions
#rangetolist := range -> [seq(i, i = range)];
#isinrange := (x, range) -> member(x, rangetolist(range));
isinrange := (x, range) -> evalb((op(1, range) <= x) and (x <= op(2, range)));

# Print function call and result
'isinrange(k, intrange)';%;

quit()
