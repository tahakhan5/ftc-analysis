close all
figure;
hold on
subplot(2,2,1)
ages;
subplot(2,2,2)
incomes;
subplot(2,2,3)
education;
subplot(2,2,4)
unemployment;
set(gcf, 'PaperPosition', [0 0 14 9]); %Position plot at left hand corner with width 5 and height 5.
set(gcf, 'PaperSize', [14 9]); %Set the paper to have width 5 and height 5.
%axis([0 128 0 280])
saveas(gcf, 'demographics', 'pdf') %Save figure
% % Reporting Dates CDF