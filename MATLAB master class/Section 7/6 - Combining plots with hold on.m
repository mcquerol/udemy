x = 0:0.2:10; 

y1 = sin(x);

plot(x,y1); 

hold on

y2 = sin(x/2); 

plot(x,y2); 
 
plot(x,y2);

y3 = 2*sin(x); 

scatter(x,y3)

bar(x,y3)


