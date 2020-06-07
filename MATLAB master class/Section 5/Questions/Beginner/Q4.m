A=rand(10)
%B=A(5:1:end-1,5:1:end-1); this does not work because it STARTS at 5, not
%after 5, must start at 6. This line ignores the last row and column and is
%not the right answer
B=A(6:end,6:end)
disp(B);