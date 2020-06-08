
a=rand(5);
ur=a(1,end); %upper right
ul=a(1,1); %upper left
lr=a(end,end); %lower right
ll=a(end,1); %lower left

R=[a(1,1) a(1,end); a(end,1) a(end,end)];
