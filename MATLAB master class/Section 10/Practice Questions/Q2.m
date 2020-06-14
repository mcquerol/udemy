clear all
sz = [3,2];
A = [1 2 3 6;
4 5 6 8;
7 8 9 10];
[rows, col] = size(A);
enlarge_matrix = zeros(rows*sz(1),col*sz(2));
for i = 1:rows
for j = 1: col
enlarge_matrix( ((i-1) * sz(1)) +1: i * sz(1), ((j-1) * sz(2)) +1: j * sz(2)) = A(i,j);
end
end