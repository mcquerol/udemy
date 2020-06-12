a=input('Enter an element in the array\n');
for j=2:length(a)
    if a(j) > a(j-1)
        flag=0;
    else
        flag=1;
        fprintf('Not monotonically increasing');
        break;
    end
end
if flag==0
   fprintf('Monitically increasing'); 
end