clc
close all
prop = []


cyber_dots = []
reg_dots = []


cur = data(1);
temp_c = [cyber(1)];
temp_r = [reg(1)];


for n = 2:length(data)
    
    if (data(n) == cur)
        temp_c = [temp_c cyber(n)];
        temp_r = [temp_r reg(n)];
    else
        prop = [prop data(n-1)]
        cyber_dots = [cyber_dots mean(temp_c)];
        reg_dots = [reg_dots mean(temp_r)];
        
        temp_c = [cyber(n)];
        temp_r = [cyber(n)];
        cur = data(n);
    end
end

scatter(prop, cyber_dots,'*')
