x = [1,2];
% 
% y = [1,2,3,4;...
%      5,6,7,8];
y = [33.35, 66.64; 82.18 17.81];

figure;
b = barh(x,y,'stacked', 'r', 'EdgeColor',[0 0 0],'LineWidth',1.5, 'BarWidth', 0.5); % stacks values in each row together
b(2).FaceColor = 'b';
axis([0 100 0 3])
set(gca, 'FontSize', 20)
ylabel('Fraud Type Cyber Regular', 'FontSize', 20)
set(gca,'yticklabel',{[]}) 
xlabel('Percentage', 'FontSize', 20)
legend('Online', 'Offline', 'Location','northeast', 'FontSize', 25)


set(gcf, 'PaperPosition', [0 0 10 4]); %Position plot at left hand corner with width 5 and height 5.
set(gcf, 'PaperSize', [10 4]); %Set the paper to have width 5 and height 5.
%axis([0 128 0 280])
saveas(gcf, 'reporting methods', 'pdf') %Save figure

