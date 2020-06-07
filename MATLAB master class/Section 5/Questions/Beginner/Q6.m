A = [5 8 8 8 9 9 6 6 5 5 4 1 2 3 5 3 3 ];
T = tabulate(A);
[a, b] = sort(T(:,3),'descend');
T(b,:);
disp(a); %values of percentages
disp(b); %indexes of percentages
disp(T); %final sorted percentages matrix (in descending order)