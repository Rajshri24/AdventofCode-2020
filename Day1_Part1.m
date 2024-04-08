clc
close all
clear all

inp = importdata('input.txt');
len = length(inp); 
sum = zeros(len-1,len-1);

for i = 1:len-1
    for j = i+1:len-1
        sum = inp(i)+inp(j);
        if sum==2020
            num1 = inp(i);
            num2 = inp(j);
        end
    end
end

ans = num1*num2;



