inp = importdata('input.txt');
len = length(inp); 
sum = zeros(len-1,len-1);

for i = 1:len-1
    for j = i+1:len-1
        for k = i+2:len-1
            sum = inp(i)+inp(j)+inp(k);
            if sum == 2020
                num1 = inp(i);
                num2 = inp(j);
                num3 = inp(k);
                ans = num1*num2*num3
            end
        end
    end
end
