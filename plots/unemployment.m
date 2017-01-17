% unpomes
% Load unps
clear all
load('10.mat')

% create bins 0-30 30-40 40-50 50 >
cyber_bins = [0 0 0 0 0];

reg_bins = [0 0 0 0 0];

unp_tot = [0 0 0 0 0];


for n = 1:length(unp)
    
    
    if (unp(n) <= 3)
        cyber_bins(1) = cyber_bins(1) + cyber(n); reg_bins(1) = reg_bins(1) + reg(n);
        unp_tot(1) = unp_tot(1)+1;
    end
    
    if (unp(n) > 3 && unp(n) <= 5)
        cyber_bins(2) = cyber_bins(2) + cyber(n); reg_bins(2) = reg_bins(2) + reg(n);
        unp_tot(2) = unp_tot(2)+1;
    end
        
    if (unp(n) > 5 && unp(n) <= 10)
        cyber_bins(3) = cyber_bins(3) + cyber(n); reg_bins(3) = reg_bins(3) + reg(n);
        unp_tot(3) = unp_tot(3)+1;
    end 
    
    if (unp(n) > 10 && unp(n) <= 15)
        cyber_bins(4) = cyber_bins(4) + cyber(n); reg_bins(4) = reg_bins(4) + reg(n);
        unp_tot(4) = unp_tot(4)+1;
    end 
    
    if (unp(n) > 15)
        cyber_bins(5) = cyber_bins(5) + cyber(n); reg_bins(5) = reg_bins(5) + reg(n);
        unp_tot(5) = unp_tot(5)+1;
    end    
end

r =reg_bins./unp_tot
c= cyber_bins./unp_tot
x = [c;r]'
b = bar(x, 'r', 'EdgeColor',[0 0 0],'LineWidth',0.5, 'BarWidth', 0.5)
b(2).FaceColor = 'b';

axis([0.5 5.5 0 5.5])
labels = {'0-3','3-5','5-10','10-15','15+'};
set(gca, 'XTick', 1:5, 'XTickLabel', labels);
set(gca,'FontSize', 20);
xlabel({'Unemployment Rate';' ';'(d)'}', 'FontSize', 23)

ylabel({'Fraud Rate'}, 'FontSize', 23)
legend('Cyber','Regular', 'Location','northeast', 'Orientation', 'horizontal')

