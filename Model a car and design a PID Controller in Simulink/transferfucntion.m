num=[0.25];
den=[493e-9 5.3e-3];
tf(num,den);
g=zpk(tf);
step(g);
