# b) Same as a) but with 1-D calling sequence
# Summary: e.g. sum(f, n) is equivalent to sum(f, k=1..n-1) 
sum(k, k=1..n-1);
simplify(%); 
sum(k, k);
sum(k^p*x^k, k=1..n-1);
simplify(%);
sum(k^p*x^k, k);
