% d = csvread('data.csv');
% r = d(gt(d(:,2),3));
% 
% if exist('Results') == 7
%     csvwrite('Results\reduced_data.csv',Z);
% else
%     mkdir Results
%     csvwrite('Results\reduced_data.csv',Z);
% end

X = csvread('data.csv');
Y = X(:,2) > 3.0;
Z = X(Y,:);
if exist('Results') == 7
csvwrite('Results\reduced_data.csv',Z);
else
mkdir Results
csvwrite('Results\reduced_data.csv',Z);
end