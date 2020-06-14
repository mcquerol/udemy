function X = string_multiplication(str, N)
X=cell(1,N);
    for i=1:N
       X(i)=str;
    end
    X=join(X);
    X=replace(X,' ','');
end