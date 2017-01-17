
% Days CDF
load('6.mat')

[f_cyber,x_cyber] = ecdf(cyber_6);
[f_reg,x_reg] = ecdf(regular_6);

figure;
plot(x_cyber, f_cyber ,'r--', 'LineWidth', 2);
hold on
plot(x_reg, f_reg ,'b', 'LineWidth', 2);
set(gca,'FontSize', 24)
axis([0 300 0 1])
axis square
legend('Cyber','Regular', 'Location','southeast', 'FontSize', 24)

grid on
xlabel('Number of Days', 'FontSize', 24)
ylabel('Distribution', 'FontSize', 24)

set(gcf, 'PaperPosition', [0 0 7 6]); %Position plot at left hand corner with width 5 and height 5.
set(gcf, 'PaperSize', [7 6]); %Set the paper to have width 5 and height 5.
%axis([0 128 0 280])
saveas(gcf, 'days', 'pdf') %Save figure
% Reporting Dates CDF