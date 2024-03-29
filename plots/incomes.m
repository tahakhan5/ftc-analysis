% incomes
% Load incs
clear all
load('8.mat')

% create bins 0-30 30-40 40-50 50 >
cyber_bins = [0 0 0 0 0];

reg_bins = [0 0 0 0 0];

inc_tot = [0 0 0 0 0];


for n = 1:length(inc)
    
    
    if (inc(n) <= 30000)
        cyber_bins(1) = cyber_bins(1) + cyber(n); reg_bins(1) = reg_bins(1) + reg(n);
        inc_tot(1) = inc_tot(1)+1;
    end
    
    if (inc(n) > 30000 && inc(n) <= 50000)
        cyber_bins(2) = cyber_bins(2) + cyber(n); reg_bins(2) = reg_bins(2) + reg(n);
        inc_tot(2) = inc_tot(2)+1;
    end
        
    if (inc(n) > 50000 && inc(n) <= 70000)
        cyber_bins(3) = cyber_bins(3) + cyber(n); reg_bins(3) = reg_bins(3) + reg(n);
        inc_tot(3) = inc_tot(3)+1;
    end 
    
    if (inc(n) > 70000 && inc(n) <= 90000)
        cyber_bins(4) = cyber_bins(4) + cyber(n); reg_bins(4) = reg_bins(4) + reg(n);
        inc_tot(4) = inc_tot(4)+1;
    end 
    
    if (inc(n) > 90000)
        cyber_bins(5) = cyber_bins(5) + cyber(n); reg_bins(5) = reg_bins(5) + reg(n);
        inc_tot(5) = inc_tot(5)+1;
    end    
end


r= reg_bins./inc_tot
c = cyber_bins./inc_tot
x = [c;r]'
b = bar(x, 'r', 'EdgeColor',[0 0 0],'LineWidth',0.5, 'BarWidth', 0.5)
b(2).FaceColor = 'b';




axis([0.5 5.5 0 2.25])
labels = {'0-30','30-50','50-70','70-90','90+'};
set(gca, 'XTick', 1:5, 'XTickLabel', labels);
set(gca,'FontSize', 20);
xlabel({'Incomes (thousands)';' ';'(b)'}', 'FontSize', 23)


ylabel({'Complaint Rate'}, 'FontSize', 23)








