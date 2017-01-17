% holoiday crimes
cyb_h =sum(cyber(349:369))
reg_h =sum(reg(349:369))

%regular crimes
cyb_n =sum(cyber(227:247))
reg_n =sum(reg(227:247))

y = [  cyb_h reg_h;  cyb_n reg_n;];
% 
b = barh(y, 'r', 'EdgeColor',[0 0 0],'LineWidth',1.5, 'BarWidth', 0.5)
% 
b(2).FaceColor = 'b';

legend('Cyber','Regular', 'Location','southeast', 'FontSize', 20)
xlabel('Number of Fraud Reports', 'FontSize', 20)
ylabel(' Holiday         Working', 'FontSize', 20)
% 
set(gca,'yticklabel',{[]}) 
set(gca,'FontSize', 20)
set(gcf, 'PaperPosition', [0 0 10 7]); %Position plot at left hand corner with width 5 and height 5.
set(gcf, 'PaperSize', [10 7]); %Set the paper to have width 5 and height 5.
saveas(gcf, 'reg_vs_holiday', 'pdf') %Save figure