h = animatedline; 

x = 1:1000; 
y = x.^2; 

for i=1:length(x)
	addpoints(h,x(i),y(i)); 
	drawnow;
end 
