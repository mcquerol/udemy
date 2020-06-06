%Defining the currencies
Q = 0.25; %quarter
d = 0.10; %dime
n = 0.05; %nickel
p = 0.01; %penny

%Matrix, each column is one person
A = [1 0 0 0; 0 1 0 0; 1 1 1 0];
sum = (A(:,1).*Q)+(A(:,2).*d)+(A(:,3).*n)+(A(:,4).*p);
[most_money,i] = max(sum);
disp("person "+i+" has "+money+" USD");
