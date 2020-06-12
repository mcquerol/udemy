
in = input('Enter size\n');
z=zeros(in);
for i=1:length(z)
    z(1:2:end,j)=0;
    for j=1:length(z)
        z(1:2:end,j)=1;
    end
end
disp(z);

% n = input('Enter the size of the matrix');
% x = zeros(n);
% for i=1:n
%     if rem(i,2)== 0
%         x(i,1:2:end) = 1;
%     else
%         x(i,2:2:end) = 1;
%     end
% end