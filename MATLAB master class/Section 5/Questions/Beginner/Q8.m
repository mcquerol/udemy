A = randperm(100,10)
A1 = length(A(A<=25))
A2 = length(A(A>25 & A<=75))
A3 = length(A(A>75 & A<=100))

    