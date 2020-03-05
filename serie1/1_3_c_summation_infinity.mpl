# c) Repeat a) and sum up to infinity 
# Obvious diverging serieses are evaluated as infinity while open expressions are displayed in symbolic form 

sum(k, k=1..infinity); 
simplify(%);
sum(k^2, k=1..infinity);
simplify(%);
sum(k^3, k=1..infinity);
simplify(%);

sum(1/k, k=1..infinity);
simplify(%);
sum(1/k^2, k=1..infinity);
simplify(%);

sum(x^k, k=1..infinity);
simplify(%);
sum(k*x^k, k=1..infinity);
simplify(%);
sum(k^2*x^k, k=1..infinity);
simplify(%);
sum(k^p*x^k, k=1..infinity);
simplify(%);
