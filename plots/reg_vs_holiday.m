% holoiday crimes
cyb_h =sum(cyber(349:369))
reg_h =sum(reg(349:369))

%regular crimes
cyb_n =sum(cyber(227:247))
reg_n =sum(reg(227:247))

y = [cyb_n reg_n; cyb_h reg_h;];
b = bar(y, 'r', 'EdgeColor',[0 0 0],'LineWidth',1.5, 'BarWidth', 0.5)

b(2).FaceColor = 'b';
legend('Cyber','Regular', 'Location','northeast', 'FontSize', 25)
set(gca,'FontSize', 11)
set(gca,'xtick',[])
set(gcf, 'PaperPosition', [0 0 10 6]); %Position plot at left hand corner with width 5 and height 5.
set(gcf, 'PaperSize', [10 6]); %Set the paper to have width 5 and height 5.
%axis([0 128 0 280])
saveas(gcf, 'reg_vs_holiday', 'pdf') %Save figure