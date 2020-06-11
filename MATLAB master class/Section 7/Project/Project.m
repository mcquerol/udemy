my_text=fileread('C:\Users\Mateo C. Querol\Desktop\MATLAB\Udemy\MATLAB master class course\Section 7\Project\sample.txt');
my_text=string(my_text);
my_text=splitlines(my_text);
my_text=replace(my_text,{'.', ',', ':', '/','"', '"'},'');
my_text=strip(my_text);
my_text=join(my_text);
my_text=split(my_text);

x=tabulate(my_text);

% X=sort(categorical(x(1:10,1)),'descend');
% Y=sort(cell2mat(x(1:10,2)),'descend');
[freq, index] = sort(cell2mat(x(:,2)),'descend');
X=categorical(x(index(1:10),1));
Y=cell2mat(x(index(1:10),2));
bar(X,Y)