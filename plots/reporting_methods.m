x = [1,2];
% 
% y = [1,2,3,4;...
%      5,6,7,8];
y = [33.35, 66.64; 82.18 17.81];

figure;
barh(x,y,'stacked'); % stacks values in each row together
title('Stacked Style')

