A = [8 9 10 11];
B = [5];
C = [9 8 5];
max_length = max([length(A), length(B),length(C)]);
x = zeros(3,max_length);
x(1,max_length-length(A)+1:max_length) = A; %x(1,1:4)
x(2,max_length-length(B)+1:max_length) = B; %x(2,4:4)
x(3,max_length-length(C)+1:max_length) = C; %x(3,1:4)
