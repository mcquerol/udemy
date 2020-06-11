in = input('Insert text\n','s');
mytext=string(split(in));
x=mytext(end:-1:1);
a = join(x);
fprintf('The input string was \n"%s"\n \n \n', in);
fprintf('The corresponding output is \n "%s" \n',a);
