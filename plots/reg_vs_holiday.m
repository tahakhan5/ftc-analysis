% holoiday crimes
cyb_h =sum(cyber(349:369))
reg_h =sum(reg(349:369))

%regular crimes
cyb_n =sum(cyber(227:247))
reg_n =sum(reg(227:247))

% figure;[h,p] = ttest(___)
% y = [ reg_h cyb_h ; reg_n cyb_n ;];
% 
% b = barh(y, 'b', 'EdgeColor',[0 0 0],'LineWidth',1.5, 'BarWidth', 0.5)
% 
% b(2).FaceColor = 'r';
% legend('Regular','Cyber', 'Location','southeast', 'FontSize', 20)
% xlabel('Number of Fraud Reports', 'FontSize', 20)
% ylabel('    Holidays         Working Days', 'FontSize', 20)
% 
% set(gca,'yticklabel',{[]}) 
% set(gca,'FontSize', 20)
set(gcf, 'PaperPosition', [0 0 10 7]); %Position plot at left hand corner with width 5 and height 5.
set(gcf, 'PaperSize', [10 7]); %Set the paper to have width 5 and height 5.
saveas(gcf, 'reg_vs_holiday', 'pdf') %Save figure